#
# Conditional build (only one option at time makes sense; if more specified
#   - only "highest" is used):
# _with_mmx	- with MMX instructions			(i586, i686 targets)
# _with_p3mmx	- with Pentium /// MMX instructions	(i686 target)
# _with_k6	- with AMD K6 instructions		(i586 target)
# _with_k62	- with AMD K6-2/K6-3 instructions	(i586 target)
# _with_k7	- with AMD Athlon/Duron instructions	(i686 target)

Summary:	GNU arbitrary precision library
Summary(de):	Beliebige Genauigkeits-Library
Summary(es):	Biblioteca de precisi�n arbitraria de la GNU
Summary(fr):	Biblioth�que de calcul de pr�cision
Summary(pl):	Biblioteka arytmetyczna GNU
Summary(pt_BR):	Biblioteca de precis�o arbitr�ria da GNU
Summary(uk):	��̦����� GNU ��צ���ϧ ������Ԧ
Summary(ru):	���������� GNU ������������ ��������
Name:		gmp
Version:	4.0.1
Release:	2
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	ftp://ftp.gnu.org/pub/gnu/gmp/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-am_fix.patch
Patch2:		%{name}-asmcpu.patch
URL:		http://www.swox.com/gmp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgmp3

%ifarch i586
%define _cpu %{?_with_k62:k62}%{!?_with_k62:%{?_with_k6:k6}%{!?_with_k6:%{?_with_mmx:pentiummmx}%{!?_with_mmx:i586}}}
%else
%ifarch i686
%define _cpu %{?_with_p3mmx:pentium3}%{!?_with_p3mmx:%{?_with_k7:athlon}%{!?_with_k7:%{?_with_mmx:pentium2}%{!?_with_mmx:i686}}}
%else
%define _cpu %{_arch}
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
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version} 
Obsoletes:	libgmp3-devel

%description devel
The static libraries, header files and documentation for using the GNU
MP arbitrary precision library in applications.

If you want to develop applications which will use the GNU MP library,
you'll need to install the gmp-devel package.

%description -l de devel
Statische Libraries, Header Files und Dokumentation zum Benutzen der
GNU MP Library.

%description -l es devel
Estas son las bibliotecas, archivos de inclusi�n y documentaci�n para
usar la biblioteca GNU de precisi�n arbitraria en tus programas.

%description -l fr devel
Ce package comprend les biblioth�ques statiques, les fichiers
d'en-t�te et la documentation n�cessaires pour utiliser la
biblioth�que de calcul de pr�cision dans les applications.

Vous n'avez besoin de ce package que si vous comptez programmer des
applications utilisant la biblioth�que GNU MP.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do gmp. Dzi�ki temu pakietowi b�dziesz
m�g� tworzy� w�asne programy z wykorzystaniem tej biblioteki.

%description -l pt_BR devel
Estas s�o as bibliotecas, arquivos de inclus�o e documenta��o para
usar a biblioteca GNU de precis�o arbitr�ria em seus programas.

%description -l uk devel
�� ¦�̦����� ������ͦ���, ������ �� ���������æ� ��� ������������
¦�̦����� GNU ��צ���ϧ ������Ԧ � ����� ������� ���������.

%description -l ru devel
��� ���������� ������������, ������ � ������������ ��� �������������
���������� GNU ������������ �������� � ����� ����������� ����������.

%package static
Summary:	GNU Arbitrary Precision static library
Summary(pl):	Biblioteka statyczna gmp
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gmp
Summary(uk):	��̦����� GNU ��צ���ϧ ������Ԧ - �������� ¦�̦�����
Summary(ru):	���������� GNU ������������ �������� - ����������� ����������
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version} 

%description static
Static gmp library.

%description -l pl static
Biblioteka statyczna gmp.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento com gmp.

%description -l uk static
�� �������� ¦�̦����� GNU ��צ���ϧ ������Ԧ.

%description -l ru static
��� ����������� ���������� GNU ������������ ��������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--with-cpu=%{_cpu} \
	--enable-cxx \
	--enable-fft

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
