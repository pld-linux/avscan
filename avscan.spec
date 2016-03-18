Summary:	AntiVirus Scanner
Summary(pl.UTF-8):	Skaner antywirusowy
Name:		avscan
Version:	5.1.1
Release:	2
License:	GPL v2 with OpenSSL exception
Group:		X11/Applications
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}-openssl.tar.bz2
# Source0-md5:	e8e76867fbdf4ddef9504b604db95667
Patch0:		%{name}-verbose.patch
URL:		http://freecode.com/projects/avscan
BuildRequires:	clamav-devel
BuildRequires:	endeavour-devel >= 3
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libstdc++-devel
Requires:	endeavour >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVScan is an anti-virus scanner that uses the ClamAV library
(libclamav) and GTK+ 1.2. It allows you to create a list of scan items
for frequently scanned locations and features on-demand virus database
updating, manual drag and drop object scanning, and pausing and
resuming of scanning, all in a simple GUI environment.

%description -l pl.UTF-8
AVScan to skaner antywirusowy wykorzystujący bibliotekę narzędzia
ClamAV (libclamav) oraz GTK+ 1.2. Pozwala na tworzenie list elementów
do regularnego skanowania, umożliwia uaktualnianie na żądanie bazy
danych wirusów, ręczne przeciąganie obiektów do przeskanowania,
zatrzymywanie i wznawianie skanowania - wszystko w prostym środowisku
graficznym.

%prep
%setup -q -n %{name}-%{version}-openssl
%patch0 -p1

%build
./configure Linux
%{__make} \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall \
		`gtk-config --cflags` \
		-DHAVE_CLAMAV `clamav-config --cflags` \
		-DHAVE_LIBENDEAVOUR2 `endeavour2-base-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	EDV_BIN_DIR=$RPM_BUILD_ROOT%{_libdir}/endeavour2/bin \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTBINFLAGS="-m755"

# fix symlink to buildroot
ln -sf ../%{_lib}/endeavour2/bin/avscan $RPM_BUILD_ROOT%{_bindir}/avscan

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man1/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/avscan
%attr(755,root,root) %{_libdir}/endeavour2/bin/avscan
%{_datadir}/endeavour2/help/avscan
%{_mandir}/man1/avscan.1*
