Summary:	GNU arbitrary precision library
Summary(pl):	Biblioteka arytmetyczna GNU
Name:		gmp
Version:	2.0.2
Release:	10
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
PreReq:		/sbin/install-info

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
/sbin/install-info %{_infodir}/gmp.info.gz /usr/info/dir

%preun devel
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/gmp.info.gz /etc/info-dir
fi

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

%changelog
* Wed Apr 28 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.2-10]
- standarized {un}registering info pages (added gmp-info.patch),
- /sbin/ldconfig is now runed as -p parameter in %post{un},
- added static subpackage,
- added stripping shared libraries.

* Sat Mar 14 1999 David Kuestler <kuestler@zeta.org.au>
- Patch for PowerPC ( Power Mac )

* Thu Feb 18 1999 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Add bugfix patches from gmp homepage. (These are supposed to go into
  gmp-2.0.3 when it is finally released.)
- Change the files section to use %attr tags (now buildable by non-root)
- Add a Prefix: tag.
- Change the Copyright to LGPL.
- Change the URL to the gmp homepage.

* Thu Feb 11 1999 Michael Johnson <johnsonm@redhat.com>
- include the private header file gmp-mparam.h because several
  apps seem to assume that they are building against the gmp
  source tree and require it.  Sigh.

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- libtoolize to work on arm

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- yet another touch of the spec file

* Wed Sep  2 1998 Michael Fulbright <msf@redhat.com>
- looked over before inclusion in RH 5.2

* Sat May 24 1998 Dick Porter <dick@cymru.net>
- Patch Makefile.in, not Makefile
- Don't specify i586, let configure decide the arch

* Sat Jan 24 1998 Marc Ewing <marc@redhat.com>
- started with package from Toshio Kuratomi <toshiok@cats.ucsc.edu>
- cleaned up file list
- fixed up install-info support
