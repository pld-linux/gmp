Summary:	GNU arbitrary precision library
Summary(pl):	Biblioteka arytmetyczna GNU
Name:		gmp
Version:	2.0.2
Release:	11
Copyright:	LGPL 
Group:		Libraries
Group(pl):	Biblioteki
URL:		http://www.matematik.su.se/~tege/gmp/
Source:		ftp://ftp.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		gmp-shared.patch
Patch1:		http://www.matematik.su.se/~tege/gmp/mpf-conversions.diff.gz
Patch2:		http://www.matematik.su.se/~tege/gmp/gmp2.0.2p2.txt
Patch3:		http://www.matematik.su.se/~tege/gmp/gmp2.0.2p3.txt
Patch4:		http://www.matematik.su.se/~tege/gmp/gmp2.0.2p4.txt
Patch5:		http://www.matematik.su.se/~tege/gmp/gmp2.0.2p5.txt
Patch6:		http://www.matematik.su.se/~tege/gmp/gmp2.0.2p6.txt
Patch7:		http://www.matematik.su.se/~tege/gmp/gmp2.0.2p7.txt
Patch8:		gmp-powerpc.patch
Patch9:		gmp-info.patch
Patch10:	gmp-DESTDIR.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is the GNU arbitrary precision library. Linking against it gives access
to functions for handling arbitrarily large numbers with either a high level
or a low level interface.

%description -l pl

Pakiet zawiera bibliotekê arytmetyczn± wysokiej precyzji. Daje ona dostêp do
szerokiego grona szybkich funkcji arytmetycznych dzia³aj±cych na liczbach
ca³kowitych, rzeczywistych i zmiennoprzecinkowych.

%package devel
Summary:	GNU Arbitrary Precision header files, static libraries, and documentation.
Summary(pl):	Pliki nag³ówkowe i dokumentacja.
Group:		Libraries
Prereq:		/usr/sbin/fix-info-dir

%description devel
These are the static libraries, header files, and documentation for using
the GNU arbitrary precision library in your own programs. With these, you
can create your own own programs that use this library.

%description -l pl devel
Pliko nag³ówkowe i dokumentacji do gmp. Dziêki temu pakietowi bêdziesz
móg³ tworzyæ w³asne programy z wykorzystaniem bblioteki arbitralnej z GNU.

%package static
Summary:	GNU Arbitrary Precision static library.
Summary(pl):	Biblioteka statyczna.
Group:		Libraries
Requires:	%{name} = %{version} 

%description static
Static library

%description -l pl static
Biblioteka statyczna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cd mpq
%patch2 -p0
cd ../mpn
%patch3 -p0
cd ../mpz/tests
%patch4 -p0
cd ../..
%patch5 -p1
cd mpq
%patch6 -p0
cd ../mpz
%patch7 -p0
cd ..
%patch8  -p1
%patch9  -p1
%patch10 -p1

%build
%configure 
make CC="gcc" CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	infodir=%{_infodir} \
	libdir=%{_libdir} \
	includedir=%{_includedir}

install mpn/gmp-mparam.h ${RPM_BUILD_ROOT}%{_includedir}/

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/gmp.info*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc SPEED NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_infodir}/gmp.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
