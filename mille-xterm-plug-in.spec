%define svn 2137

Summary:	Mille-Xterm Pluing for Netscape/Mozilla
Name:		mille-xterm-plug-in
Version:	1.0
Release:	%mkrel 0.%{svn}.4
License:	GPL
Group:		Networking/WWW
URL:		http://www.revolutionlinux.com/mille-xterm/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	X11-devel
BuildRequires:	mozilla-firefox-devel
BuildRequires:	gtk2-devel
BuildRequires:	nspr-devel >= 2:1.0.7
BuildRequires:	nss-devel >= 2:1.0.7
BuildRequires:	pkgconfig
BuildRequires:  mozilla-firefox
BuildRequires:  flex
Provides:	mille-xterm-plug-in
Requires:	mozilla-firefox
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
mille-xterm-plug-in is a Mozilla browser plugin to allow playing embedded
movies on web pages.

%prep

%setup -q

# antibork
perl -pi -e "s|firefox-plugin|mozilla-firefox-plugin|g" configure*

%build
chmod 755 configure

export CPPFLAGS="%{optflags} `pkg-config --cflags mozilla-nspr` `pkg-config --cflags mozilla-nss` `pkg-config --cflags firefox-plugin`"

%configure2_5x \
    --with-gecko-sdk=%{_prefix}

# weirdness...
perl -pi -e "s|-lxpcomglue||g" Makefile

%make

perl -pi -e "s|which mozilla|which mozilla-firefox|g" install.sh

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}

%makeinstall_std libdir=%{_libdir}

%find_lang xtermplug-in

%clean
rm -rf %{buildroot}

%files -f xtermplug-in.lang
%defattr (-,root,root)
%doc ChangeLog INSTALL README
%config(noreplace) %{_sysconfdir}/xtermplug-in.conf
%config(noreplace) %{_sysconfdir}/xtermplug-in.types
%{_libdir}/mozilla/plugins/xtermplug-in.so
%{_libdir}/mozilla/plugins/xtermplug-in.xpt


