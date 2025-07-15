Summary:	Set of Vapoursynth filtes that can be used for inverse telecine
Summary(pl.UTF-8):	Zestaw filtrów Vapoursynth, które można użyć do odwrotnego procesu telekina
Name:		vapoursynth-plugin-vivtc
Version:	1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/vapoursynth/vivtc/archive/R%{version}/vivtc-R%{version}.tar.gz
# Source0-md5:	49f2890f78878b9540e6fd767331a4ed
Patch0:		vivtc-meson.patch
URL:		https://github.com/vapoursynth/vivtc
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIVTC is a set of filters that can be used for inverse telecine. It is
a rewrite of some of tritical's TIVTC filters.

%description -l pl.UTF-8
VIVTC to zbiór filtrów, które można wykorzystać do odwrotnego procesu
telekina. Jest to przepisana część filtrów TIVTC tritical.

%prep
%setup -q -n vivtc-R%{version}
%patch -P0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/vivtc.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libvivtc.so
