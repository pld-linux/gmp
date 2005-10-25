Summary:	GNU arbitrary precision library
Summary(de):	Beliebige Genauigkeits-Library
Summary(es):	Biblioteca de precisi�n arbitraria de la GNU
Summary(fr):	Biblioth�que de calcul de pr�cision
Summary(pl):	Biblioteka arytmetyczna GNU
Summary(pt_BR):	Biblioteca de precis�o arbitr�ria da GNU
Summary(uk):	��̦����� GNU ��צ���ϧ ������Ԧ
Summary(ru):	���������� GNU ������������ ��������
Name:		gmp
Version:	4.1.4
Release:	3
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/gmp/%{name}-%{version}.tar.gz
# Source0-md5:	aa5e5fb3a7cdebe8c5b681a6cf4a670e
Patch0:		%{name}-info.patch
Patch1:		%{name}-gcc-version.patch
Patch2:		%{name}-amd64.patch
Patch3:		%{name}-acinclude.patch
Patch4:		%{name}-sparc64.patch
Patch5:		%{name}-cmpi.patch
# http://www.swox.com/gmp/#STATUS
Patch6:		%{name}-site.patch
URL:		http://www.swox.com/gmp/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libstdc++-devel
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

%description -l de
Das gmp-paket enth�lt GNU MP, eine Library f�r Arithmetik bei
beliebiger Genauigkeit, Operationen mit Intergern mit Vorzeichen,
Rationale Zahlen, und Floating Point-Zahlen. GNU MP wurde f�r
Geschwindigkeit sowohl f�r kleine als auch f�r sehr gro�e Operanden
optimiert. GNU MP ist aus mehreren Gr�nden schnell: Es benutzt
fullwords als grundlegenden Arithmetik-Typ, benutzt schnelle
Algorithmen, und benutzt Assembler-Code f�r verschiedene CPUs, und
legt mehr Wert auf Geschwindigkeit als auf Einfachheit der Funktionen.

Installieren Sie das gmp-Paket, wenn Sie eine schnelle Library f�r
beliebige Genauigket brauchen.

%description -l es
Esta es la biblioteca GNU de precisi�n arbitraria. Da acceso a
funciones para manipular arbitrariamente grandes n�meros con
interfaces de alto o bajo nivel.

%description -l fr
Ce package contient la biblioth�que GNU MP. Cette derni�re permet de
calculer avec une grande pr�cision sur des nombres entiers, rationnels
ou m�me des fractions, sign�s ou non. GNU MP a �t� con�ue pour �tre
rapide pour les petits nombres ainsi que les tr�s grands gr�ce �
plusieurs techniques (calcul sur plusieurs chiffres hexa simultan�s,
algorithmes optimis�s, utilisation de l'assembleur pour les routines
critiques) parfois au d�triment de la simplicit� ou l'�l�gance.

Installez ce package si vous avez besoin d'une biblioth�que de calcul
de pr�cision rapide

%description -l pl
Pakiet zawiera bibliotek� arytmetyczn� wysokiej precyzji. Daje ona
dost�p do szerokiego grona szybkich funkcji arytmetycznych
dzia�aj�cych na liczbach ca�kowitych, rzeczywistych i
zmiennoprzecinkowych.

%description -l pt_BR
Esta � a biblioteca GNU de precis�o arbitr�ria. Ela d� acesso a
fun��es para manipular arbitrariamente grandes n�meros com interfaces
de alto ou baixo n�vel.

%description -l uk
�� ¦�̦����� GNU ��צ���ϧ ������Ԧ. �¦��� ������� � ��� ����� ���
��������� ������ �� ����æ� ��� ������ � �� �������� �������� �������
����� ���������� �� �������� ��� � �������� Ҧ���.

%description -l ru
��� ���������� GNU ������������ ��������. ������ � ��� �������������
������ � �������� ��� ������ �� ����� ������ �������� ������� ���
����� �����-, ��� � ����� ��������������� ���������.

%package devel
Summary:	GNU Arbitrary Precision header files, static libraries, and documentation
Summary(de):	Entwicklungstools f�r GNU MP
Summary(es):	Archivos de inclusi�n, bibliotecas y documentaci�n de la biblioteca gmp
Summary(fr):	Outils de d�veloppement pour la biblioth�que de calcul GMP
Summary(pl):	Pliki nag��wkowe i dokumentacja do biblioteki gmp
Summary(pt_BR):	Arquivos de inclus�o, bibliotecas e documenta��o da biblioteca gmp
Summary(uk):	����������� �������� ��� ¦�̦����� GNU ��צ���ϧ ������Ԧ
Summary(ru):	����������� ���������� ��� ���������� GNU ������������ ��������
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
Estas son las bibliotecas, archivos de inclusi�n y documentaci�n para
usar la biblioteca GNU de precisi�n arbitraria en tus programas.

%description devel -l fr
Ce package comprend les biblioth�ques statiques, les fichiers
d'en-t�te et la documentation n�cessaires pour utiliser la
biblioth�que de calcul de pr�cision dans les applications.

Vous n'avez besoin de ce package que si vous comptez programmer des
applications utilisant la biblioth�que GNU MP.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do gmp. Dzi�ki temu pakietowi mo�na
tworzy� w�asne programy z wykorzystaniem tej biblioteki.

%description devel -l pt_BR
Estas s�o as bibliotecas, arquivos de inclus�o e documenta��o para
usar a biblioteca GNU de precis�o arbitr�ria em seus programas.

%description devel -l uk
�� ¦�̦����� ������ͦ���, ������ �� ���������æ� ��� ������������
¦�̦����� GNU ��צ���ϧ ������Ԧ � ����� ������� ���������.

%description devel -l ru
��� ���������� ������������, ������ � ������������ ��� �������������
���������� GNU ������������ �������� � ����� ����������� ����������.

%package static
Summary:	GNU Arbitrary Precision static library
Summary(pl):	Biblioteka statyczna gmp
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gmp
Summary(uk):	��̦����� GNU ��צ���ϧ ������Ԧ - �������� ¦�̦�����
Summary(ru):	���������� GNU ������������ �������� - ����������� ����������
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmp library.

%description static -l pl
Biblioteka statyczna gmp.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com gmp.

%description static -l uk
�� �������� ¦�̦����� GNU ��צ���ϧ ������Ԧ.

%description static -l ru
��� ����������� ���������� GNU ������������ ��������.

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
Summary(pl):	Biblioteka arytmetyczna GNU - pliki nag��wkowe interfejsu C++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
Header files for C++ class interface to GNU arbitrary precision
library.

%description c++-devel -l pl
Pliki nag��wkowe interfejsu w postaci klas C++ do biblioteki
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

%package -n libmpfr-devel
Summary:	A library for multiple-precision floating-point computations with exact rounding
Summary(pl):	Biblioteka oblicze� zmiennoprzecinkowych z wielokrotn� precyzj� i dok�adnym zaokr�glaniem
Group:		Development/Libraries

%description -n libmpfr-devel
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library and should replace the MPF
class in further releases of GMP. The main goal of MPFR is to provide
a library for multiple-precision floating-point computation which is
both efficient and has a well-defined semantics. It copies the good
ideas from the ANSI/IEEE-754 standard for double-precision
floating-point arithmetic (53-bit mantissa).

%description -n libmpfr-devel -l pl
Biblioteka MPFR to biblioteka C do oblicze� zmiennoprzecinkowych z
wielokrotn� precyzj� i dok�adnym zaokr�glaniem (zwanym tak�e poprawnym
zaokr�glaniem). Jest oparta na bibliotece GMP wielokrotnej precyzji i
powinna zast�pi� klas� MPF w kolejnych wydaniach GMP. G��wnym celem
MPFR jest dostarczenie biblioteki do oblicze� zmiennoprzecinkowych
wielokrotnej precyzji, kt�ra jest wydajna i ma dobrze zdefiniowan�
semantyk�. Powiela dobre idee ze standardu ANSI/IEEE-754 dla
arytmetyki zmiennoprzecinkowej podw�jnej precyzji (z 53-bitow�
mantys�).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0

%build
%{__libtoolize}
%{__aclocal} -I mpfr
%{__autoconf}
%{__automake}
%configure \
	--with-cpu=%{_target_cpu} \
	--enable-cxx \
	--enable-fft \
	--enable-mpfr

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

%post -n libmpfr-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n libmpfr-devel
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

%files -n libmpfr-devel
%defattr(644,root,root,755)
%{_includedir}/mpf2mpfr.h
%{_includedir}/mpfr*.h
%{_libdir}/libmpfr.a
%{_infodir}/mpfr.info*
