#
# Conditional build (only one option at time makes sense; if more specified
#   - only "highest" is used):
%bcond_with	mmx	# with MMX instructions			(i586, i686 targets)
%bcond_with	p3mmx	# with Pentium /// MMX instructions	(i686 target)
%bcond_with	k6	# with AMD K6 instructions		(i586 target)
%bcond_with	k62	# with AMD K6-2/K6-3 instructions	(i586 target)
%bcond_with	k7	# with AMD Athlon/Duron instructions	(i686 target)
#
Summary:	GNU arbitrary precision library
Summary(de):	Beliebige Genauigkeits-Library
Summary(es):	Biblioteca de precisión arbitraria de la GNU
Summary(fr):	Bibliothèque de calcul de précision
Summary(pl):	Biblioteka arytmetyczna GNU
Summary(pt_BR):	Biblioteca de precisão arbitrária da GNU
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ GNU ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦
Summary(ru):	âÉÂÌÉÏÔÅËÁ GNU ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ
Name:		gmp
Version:	4.1.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/gmp/%{name}-%{version}.tar.gz
# Source0-md5:	bdbb9136fa22a0ccf028d0f87aae1dd2
Patch0:		%{name}-info.patch
Patch1:		%{name}-asmcpu.patch
Patch2:		%{name}-gcc-version.patch
Patch3:		%{name}-amd64.patch
Patch4:		%{name}-acinclude.patch
Patch5:		%{name}-sparc64.patch
Patch6:		http://www.swox.com/gmp/patches/mpf_sub.c.diff
URL:		http://www.swox.com/gmp/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
Obsoletes:	libgmp3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch i586
%define _cpu %{?with_k62:k62}%{!?with_k62:%{?with_k6:k6}%{!?with_k6:%{?with_mmx:pentiummmx}%{!?with_mmx:i586}}}
%else
%ifarch i686
%define _cpu %{?with_p3mmx:pentium3}%{!?with_p3mmx:%{?with_k7:athlon}%{!?with_k7:%{?with_mmx:pentium2}%{!?with_mmx:i686}}}
%else
%define _cpu %{_target_cpu}
%endif
%endif

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

%description -l es
Esta es la biblioteca GNU de precisión arbitraria. Da acceso a
funciones para manipular arbitrariamente grandes números con
interfaces de alto o bajo nivel.

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

%description -l pt_BR
Esta é a biblioteca GNU de precisão arbitrária. Ela dá acesso a
funções para manipular arbitrariamente grandes números com interfaces
de alto ou baixo nível.

%description -l uk
ãÅ Â¦ÂÌ¦ÏÔÅËÁ GNU ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦. úÂ¦ÒËÁ ÐÒÏÇÒÁÍ Ú ÎÅÀ ÎÁÄÁ¤ ÃÉÍ
ÐÒÏÇÒÁÍÁÍ ÄÏÓÔÕÐ ÄÏ ÆÕÎËÃ¦Ê ÄÌÑ ÒÏÂÏÔÉ Ú ÑË ÚÁ×ÇÏÄÎÏ ×ÅÌÉËÉÍÉ ÞÉÓÌÁÍÉ
ÞÅÒÅÚ ¦ÎÔÅÒÆÅÊÓÉ ÑË ÎÉÚØËÏÇÏ ÔÁË ¦ ×ÉÓÏËÏÇÏ Ò¦×ÎÑ.

%description -l ru
üÔÏ ÂÉÂÌÉÏÔÅËÁ GNU ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ. óÂÏÒËÁ Ó ÎÅÊ ÐÒÅÄÏÓÔÁ×ÌÑÅÔ
ÄÏÓÔÕÐ Ë ÆÕÎËÃÉÑÍ ÄÌÑ ÒÁÂÏÔÙ ÓÏ ÓËÏÌØ ÕÇÏÄÎÏ ÂÏÌØÛÉÍÉ ÞÉÓÌÁÍÉ ËÁË
ÞÅÒÅÚ ÎÉÚËÏ-, ÔÁË É ÞÅÒÅÚ ×ÙÓÏËÏÕÒÏ×ÎÅ×ÙÊ ÉÎÔÅÒÆÅÊÓ.

%package devel
Summary:	GNU Arbitrary Precision header files, static libraries, and documentation
Summary(de):	Entwicklungstools für GNU MP
Summary(es):	Archivos de inclusión, bibliotecas y documentación de la biblioteca gmp
Summary(fr):	Outils de développement pour la bibliothèque de calcul GMP
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki gmp
Summary(pt_BR):	Arquivos de inclusão, bibliotecas e documentação da biblioteca gmp
Summary(uk):	¶ÎÓÔÒÕÍÅÎÔÉ ÒÏÚÒÏÂËÉ ÄÌÑ Â¦ÂÌ¦ÏÔÅËÉ GNU ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦
Summary(ru):	éÎÓÔÒÕÍÅÎÔÙ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ ÂÉÂÌÉÏÔÅËÉ GNU ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgmp3-devel

%description devel
The static libraries, header files and documentation for using the GNU
MP arbitrary precision library in applications.

If you want to develop applications which will use the GNU MP library,
you'll need to install the gmp-devel package.

%description devel -l de
Statische Libraries, Header Files und Dokumentation zum Benutzen der
GNU MP Library.

%description devel -l es
Estas son las bibliotecas, archivos de inclusión y documentación para
usar la biblioteca GNU de precisión arbitraria en tus programas.

%description devel -l fr
Ce package comprend les bibliothèques statiques, les fichiers
d'en-tête et la documentation nécessaires pour utiliser la
bibliothèque de calcul de précision dans les applications.

Vous n'avez besoin de ce package que si vous comptez programmer des
applications utilisant la bibliothèque GNU MP.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do gmp. Dziêki temu pakietowi bêdziesz
móg³ tworzyæ w³asne programy z wykorzystaniem tej biblioteki.

%description devel -l pt_BR
Estas são as bibliotecas, arquivos de inclusão e documentação para
usar a biblioteca GNU de precisão arbitrária em seus programas.

%description devel -l uk
ãÅ Â¦ÂÌ¦ÏÔÅËÁ ÐÒÏÇÒÁÍ¦ÓÔÁ, ÈÅÄÅÒÉ ÔÁ ÄÏËÕÍÅÎÔÁÃ¦Ñ ÄÌÑ ×ÉËÏÒÉÓÔÁÎÎÑ
Â¦ÂÌ¦ÏÔÅËÉ GNU ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦ Õ ×ÁÛÉÈ ×ÌÁÓÎÉÈ ÐÒÏÇÒÁÍÁÈ.

%description devel -l ru
üÔÏ ÂÉÂÌÉÏÔÅËÁ ÒÁÚÒÁÂÏÔÞÉËÁ, ÈÅÄÅÒÙ É ÄÏËÕÍÅÎÔÁÃÉÑ ÄÌÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ
ÂÉÂÌÉÏÔÅËÉ GNU ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ × ×ÁÛÉÈ ÓÏÂÓÔ×ÅÎÎÙÈ ÐÒÏÇÒÁÍÍÁÈ.

%package static
Summary:	GNU Arbitrary Precision static library
Summary(pl):	Biblioteka statyczna gmp
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com gmp
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ GNU ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦ - ÓÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ
Summary(ru):	âÉÂÌÉÏÔÅËÁ GNU ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ - ÓÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmp library.

%description static -l pl
Biblioteka statyczna gmp.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gmp.

%description static -l uk
ãÅ ÓÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ GNU ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦.

%description static -l ru
üÔÏ ÓÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ GNU ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ.

%package c++
Summary:	GNU arbitrary precision library - C++ interface
Summary(pl):	Biblioteka arytmetyczna GNU - interfejs C++
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ class interface to GNU arbitrary precision library.

%description c++ -l pl
Interfejs w postaci klas C++ do biblioteki arytmetycznej GNU.

%package c++-devel
Summary:	GNU arbitrary precition library - C++ interface headers
Summary(pl):	Biblioteka arytmetyczna GNU - pliki nag³ówkowe interfejsu C++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
Header files for C++ class interface to GNU arbitrary precision
library.

%description c++-devel -l pl
Pliki nag³ówkowe interfejsu w postaci klas C++ do biblioteki
arytmetycznej GNU.

%package c++-static
Summary:	GNU arbitrary precition library - C++ static library
Summary(pl):	Biblioteka arytmetyczna GNU - statyczna biblioteka C++
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static version of C++ class interface to GNU arbitrary precision
library.

%description c++-static -l pl
Statycza wersja interfejsu w postaci klas C++ do biblioteki
arytmetycznej GNU.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
patch mpf/sub.c %{PATCH6}

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I mpfr
%{__autoconf}
%{__automake}
%configure \
	--with-cpu=%{_cpu} \
	--enable-cxx \
	--enable-fft

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgmp.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmp.so
%{_libdir}/libgmp.la
%{_includedir}/gmp.h
%{_infodir}/gmp.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgmp.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmpxx.so.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmpxx.so
%{_libdir}/libgmpxx.la
%{_includedir}/gmpxx.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libgmpxx.a
