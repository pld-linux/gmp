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
Patch20:	gmp-2.0.2-powerpc.patch
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
%patch20 -p1

# The patches from the gmp homepage are a bit messy to include via the %patch
# macro.  If anyone knows a better way, they're welcome to change this...
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

%build
libtoolize --copy --force
./configure --prefix=/usr
make CFLAGS="${RPM_OPT_FLAGS}"

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/lib ${RPM_BUILD_ROOT}/usr/info \
         ${RPM_BUILD_ROOT}/usr/include

make CFLAGS="${RPM_OPT_FLAGS}" prefix=${RPM_BUILD_ROOT}/usr install
gzip -9nf ${RPM_BUILD_ROOT}/usr/info/gmp.info*
install -m 644 mpn/gmp-mparam.h ${RPM_BUILD_ROOT}/usr/include/

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/gmp.info.gz /usr/info/dir

%preun devel
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/gmp.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr ( - root root -)
%doc COPYING
/usr/lib/libgmp.so.*.*

%files devel
%defattr ( - root root -)
%doc SPEED NEWS README
/usr/lib/libgmp.so
/usr/lib/libgmp.a
/usr/include/gmp.h
/usr/include/gmp-mparam.h
/usr/info/gmp.info*

%changelog
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
