Summary:	GNU arbitrary precision library
Summary(de):	Beliebige Genauigkeits-Library
Summary(fr):	Bibliothèque de calcul de précision
Summary(pl):	Biblioteka arytmetyczna GNU
Name:		gmp
Version:	2.0.2
Release:	14
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		http://www.swox.com/gmp/mpf-conversions.diff.gz
Patch2:		http://www.swox.com/gmp/%{name}2.0.2p2.txt
Patch3:		http://www.swox.com/gmp/%{name}2.0.2p3.txt
Patch4:		http://www.swox.com/gmp/%{name}2.0.2p4.txt
Patch5:		http://www.swox.com/gmp/%{name}2.0.2p5.txt
Patch6:		http://www.swox.com/gmp/%{name}2.0.2p6.txt
Patch7:		http://www.swox.com/gmp/%{name}2.0.2p7.txt
Patch8:		http://www.swox.com/gmp/%{name}2.0.2p8.txt
Patch9:		http://www.swox.com/gmp/%{name}2.0.2p9.txt
Patch10:	%{name}-powerpc.patch
Patch11:	%{name}-info.patch
Patch12:	%{name}-DESTDIR.patch
Patch13:	%{name}-sparc.patch
URL:		http://www.swox.com/gmp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast for several reasons: It uses fullwords
as the basic arithmetic type, it uses fast algorithms, it carefully
optimizes assembly code for many CPUs' most common inner loops and it
generally emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

%description -l de
Das gmp-paket enthält GNU MP, eine Library für Arithmetik bei
beliebiger Genauigkeit, Operationen mit Intergern mit Vorzeichen,
Rationale Zahlen, und Floating Point-Zahlen. GNU MP wurde für
Geschwindigkeit sowohl für kleine als auch für sehr große Operanden
optimiert. GNU MP ist aus mehreren Gründen schnell: Es benutzt
fullwords als grundlegenden Arithmetik-Typ, benutzt schnelle
Algorithmen, und benutzt Assembler-Code für verschiedene CPUs, und
legt mehr Wert auf Geschwindigkeit als auf Einfachheit der Funktionen.

Installieren Sie das gmp-Paket, wenn Sie eine schnelle Library für
beliebige Genauigket brauchen.

%description -l fr
Ce package contient la bibliothèque GNU MP. Cette dernière permet de
calculer avec une grande précision sur des nombres entiers, rationnels
ou même des fractions, signés ou non. GNU MP a été conçue pour être
rapide pour les petits nombres ainsi que les très grands grâce à
plusieurs techniques (calcul sur plusieurs chiffres hexa simultanés,
algorithmes optimisés, utilisation de l'assembleur pour les routines
critiques) parfois au détriment de la simplicité ou l'élégance.

Installez ce package si vous avez besoin d'une bibliothèque de calcul
de précision rapide

%description -l pl
Pakiet zawiera bibliotekê arytmetyczn± wysokiej precyzji. Daje ona
dostêp do szerokiego grona szybkich funkcji arytmetycznych
dzia³aj±cych na liczbach ca³kowitych, rzeczywistych i
zmiennoprzecinkowych.

%package devel
Summary:	GNU Arbitrary Precision header files, static libraries, and documentation
Summary(de):	Entwicklungstools für GNU MP
Summary(fr):	Outils de développement pour la bibliothèque de calcul GMP
Summary(pl):	Pliki nag³ówkowe i dokumentacja
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
The static libraries, header files and documentation for using the GNU
MP arbitrary precision library in applications.

If you want to develop applications which will use the GNU MP library,
you'll need to install the gmp-devel package.

%description -l de devel
Statische Libraries, Header Files und Dokumentation zum Benutzen der
GNU MP Library.

%description -l fr devel
Ce package comprend les bibliothèques statiques, les fichiers
d'en-tête et la documentation nécessaires pour utiliser la
bibliothèque de calcul de précision dans les applications.

Vous n'avez besoin de ce package que si vous comptez programmer des
applications utilisant la bibliothèque GNU MP.

%description -l pl devel
Pliko nag³ówkowe i dokumentacji do gmp. Dziêki temu pakietowi bêdziesz
móg³ tworzyæ w³asne programy z wykorzystaniem bblioteki arbitralnej z
GNU.

%package static
Summary:	GNU Arbitrary Precision static library
Summary(pl):	Biblioteka statyczna gmp
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version} 

%description static
Static gmp library.

%description -l pl static
Biblioteka statyczna gmp.

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
cd ../mpf
%patch8 -p0
cd ../mpn/generic
%patch9 -p0
cd ../..
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
libtoolize --copy --force
%configure 
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	infodir=%{_infodir} \
	libdir=%{_libdir} \
	includedir=%{_includedir}

install mpn/gmp-mparam.h ${RPM_BUILD_ROOT}%{_includedir}/

gzip -9nf SPEED NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_infodir}/gmp.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
