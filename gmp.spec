#
# Conditional build:
%bcond_without	cxx	# don't build C++ interface
%bcond_without	tests	# don't perform tests
#
Summary:	GNU arbitrary precision library
Summary(de.UTF-8):	Beliebige Genauigkeits-Library
Summary(es.UTF-8):	Biblioteca de precisión arbitraria de la GNU
Summary(fr.UTF-8):	Bibliothèque de calcul de précision
Summary(pl.UTF-8):	Biblioteka arytmetyczna GNU
Summary(pt_BR.UTF-8):	Biblioteca de precisão arbitrária da GNU
Summary(uk.UTF-8):	Бібліотека GNU довільної точності
Summary(ru.UTF-8):	Библиотека GNU произвольной точности
Name:		gmp
Version:	4.2.2
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/gmp/%{name}-%{version}.tar.bz2
# Source0-md5:	7ce52531644e6d12f16911b7e3151f3f
Patch0:		%{name}-info.patch
Patch1:		%{name}-multilib.patch
URL:		http://gmplib.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_cxx:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	texinfo
Obsoletes:	libgmp3
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

%description -l de.UTF-8
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

%description -l es.UTF-8
Esta es la biblioteca GNU de precisión arbitraria. Da acceso a
funciones para manipular arbitrariamente grandes números con
interfaces de alto o bajo nivel.

%description -l fr.UTF-8
Ce package contient la bibliothèque GNU MP. Cette dernière permet de
calculer avec une grande précision sur des nombres entiers, rationnels
ou même des fractions, signés ou non. GNU MP a été conçue pour être
rapide pour les petits nombres ainsi que les très grands grâce à
plusieurs techniques (calcul sur plusieurs chiffres hexa simultanés,
algorithmes optimisés, utilisation de l'assembleur pour les routines
critiques) parfois au détriment de la simplicité ou l'élégance.

Installez ce package si vous avez besoin d'une bibliothèque de calcul
de précision rapide

%description -l pl.UTF-8
Pakiet zawiera bibliotekę arytmetyczną wysokiej precyzji. Daje ona
dostęp do szerokiego grona szybkich funkcji arytmetycznych
działających na liczbach całkowitych, rzeczywistych i
zmiennoprzecinkowych.

%description -l pt_BR.UTF-8
Esta é a biblioteca GNU de precisão arbitrária. Ela dá acesso a
funções para manipular arbitrariamente grandes números com interfaces
de alto ou baixo nível.

%description -l uk.UTF-8
Це бібліотека GNU довільної точності. Збірка програм з нею надає цим
програмам доступ до функцій для роботи з як завгодно великими числами
через інтерфейси як низького так і високого рівня.

%description -l ru.UTF-8
Это библиотека GNU произвольной точности. Сборка с ней предоставляет
доступ к функциям для работы со сколь угодно большими числами как
через низко-, так и через высокоуровневый интерфейс.

%package devel
Summary:	GNU Arbitrary Precision library header files and documentation
Summary(de.UTF-8):	Entwicklungstools für GNU MP
Summary(es.UTF-8):	Archivos de inclusión y documentación de la biblioteca gmp
Summary(fr.UTF-8):	Outils de développement pour la bibliothèque de calcul GMP
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do biblioteki gmp
Summary(pt_BR.UTF-8):	Arquivos de inclusão e documentação da biblioteca gmp
Summary(uk.UTF-8):	Інструменти розробки для бібліотеки GNU довільної точності
Summary(ru.UTF-8):	Инструменты разработки для библиотеки GNU произвольной точности
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgmp3-devel

%description devel
The header files and documentation for using the GNU MP arbitrary
precision library in applications.

If you want to develop applications which will use the GNU MP library,
you'll need to install the gmp-devel package.

%description devel -l de.UTF-8
Header Files und Dokumentation zum Benutzen der GNU MP Library.

%description devel -l es.UTF-8
Estas son las bibliotecas, archivos de inclusión y documentación para
usar la biblioteca GNU de precisión arbitraria en tus programas.

%description devel -l fr.UTF-8
Ce package comprend les fichiers d'en-tête et la documentation
nécessaires pour utiliser la bibliothèque de calcul de précision dans
les applications.

Vous n'avez besoin de ce package que si vous comptez programmer des
applications utilisant la bibliothèque GNU MP.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do gmp. Dzięki temu pakietowi można
tworzyć własne programy z wykorzystaniem tej biblioteki.

%description devel -l pt_BR.UTF-8
Estas são as bibliotecas, arquivos de inclusão e documentação para
usar a biblioteca GNU de precisão arbitrária em seus programas.

%description devel -l uk.UTF-8
Це бібліотека програміста, хедери та документація для використання
бібліотеки GNU довільної точності у ваших власних програмах.

%description devel -l ru.UTF-8
Это библиотека разработчика, хедеры и документация для использования
библиотеки GNU произвольной точности в ваших собственных программах.

%package static
Summary:	GNU Arbitrary Precision static library
Summary(pl.UTF-8):	Biblioteka statyczna gmp
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com gmp
Summary(uk.UTF-8):	Бібліотека GNU довільної точності - статична бібліотека
Summary(ru.UTF-8):	Библиотека GNU произвольной точности - статическая библиотека
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmp library.

%description static -l pl.UTF-8
Biblioteka statyczna gmp.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com gmp.

%description static -l uk.UTF-8
Це статична бібліотека GNU довільної точності.

%description static -l ru.UTF-8
Это статическая библиотека GNU произвольной точности.

%package bsd
Summary:	GNU arbitrary precision library - BSD-compatible MP library
Summary(pl.UTF-8):	Biblioteka arytmetyczna GNU - biblioteka MP kompatybilna z BSD
Group:		Libraries
# doesn't require base

%description bsd
This package contains BSD-compatible MP library based on GNU MP.

%description bsd -l pl.UTF-8
Ten pakiet zawiera bibliotekę MP kompatybilną z BSD opartą na GNU MP.

%package bsd-devel
Summary:	GNU arbitrary precision library - BSD-compatible MP API
Summary(pl.UTF-8):	Biblioteka arytmetyczna GNU - API MP kompatybilne z BSD
Group:		Development/Libraries
Requires:	%{name}-bsd = %{version}-%{release}

%description bsd-devel
This package contains BSD-compatible MP library header file.

%description bsd-devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy biblioteki MP kompatybilnej z BSD.

%package bsd-static
Summary:	GNU arbitrary precision library - BSD-compatible static MP library
Summary(pl.UTF-8):	Biblioteka arytmetyczna GNU - biblioteka statyczna MP kompatybilna z BSD
Group:		Development/Libraries
Requires:	%{name}-bsd-devel = %{version}-%{release}

%description bsd-static
This package contains BSD-compatible MP static library based on GNU
MP.

%description bsd-static -l pl.UTF-8
Ten pakiet zawiera bibliotekę statyczną MP kompatybilną z BSD opartą
na GNU MP.

%package c++
Summary:	GNU arbitrary precision library - C++ interface
Summary(pl.UTF-8):	Biblioteka arytmetyczna GNU - interfejs C++
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ class interface to GNU arbitrary precision library.

%description c++ -l pl.UTF-8
Interfejs w postaci klas C++ do biblioteki arytmetycznej GNU.

%package c++-devel
Summary:	GNU arbitrary precition library - C++ interface headers
Summary(pl.UTF-8):	Biblioteka arytmetyczna GNU - pliki nagłówkowe interfejsu C++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
Header files for C++ class interface to GNU arbitrary precision
library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe interfejsu w postaci klas C++ do biblioteki
arytmetycznej GNU.

%package c++-static
Summary:	GNU arbitrary precition library - C++ static library
Summary(pl.UTF-8):	Biblioteka arytmetyczna GNU - statyczna biblioteka C++
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static version of C++ class interface to GNU arbitrary precision
library.

%description c++-static -l pl.UTF-8
Statycza wersja interfejsu w postaci klas C++ do biblioteki
arytmetycznej GNU.

%prep
%setup -q
%patch0 -p1
%ifarch %{ix86} %{x8664} ppc ppc64 s390 s390x sparc sparcv9 sparc64
# ugly hack, don't apply on other archs (also recheck sizes on each upgrade)
%patch1 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-cpu=%{_target_cpu} \
	%{?with_cxx:--enable-cxx} \
	--enable-fft \
	--enable-mpbsd

%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	bsd -p /sbin/ldconfig
%postun	bsd -p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmp.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmp.so
%{_libdir}/libgmp.la
%{_includedir}/gmp.h
%{_infodir}/gmp.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgmp.a

%files bsd
%attr(755,root,root) %{_libdir}/libmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmp.so.3

%files bsd-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmp.so
%{_libdir}/libmp.la
%{_includedir}/mp.h

%files bsd-static
%defattr(644,root,root,755)
%{_libdir}/libmp.a

%if %{with cxx}
%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmpxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmpxx.so.4

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmpxx.so
%{_libdir}/libgmpxx.la
%{_includedir}/gmpxx.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libgmpxx.a
%endif
