# NOTE: obsoleted by lxsession >= 0.4.9
#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	LXPolkit - a simple PolicyKit authentication agent
Summary(pl.UTF-8):	LXPolkit - prosty agent uwierzytelniania PolicyKit
Name:		lxpolkit
Version:	0.1.0
Release:	1.1
License:	GPL v3
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	2597b00035fe1d695219e0f9bfa8c26f
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXPolkit is a simple PolicyKit authentication agent.

%description -l pl.UTF-8
LXPolkit to prosty agent uwierzytelniania PolicyKit.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify name
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{tt_RU,tt}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/frp
# just a copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
/etc/xdg/autostart/lxpolkit.desktop
%attr(755,root,root) %{_libdir}/lxpolkit
%{_datadir}/lxpolkit
