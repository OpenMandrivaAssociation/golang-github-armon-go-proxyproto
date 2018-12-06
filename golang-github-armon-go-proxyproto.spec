# https://github.com/armon/go-proxyproto
%global goipath         github.com/armon/go-proxyproto
%global commit          5b7edb60ff5f69b60d1950397f7bde6171f1807d

%gometa

Name:           golang-github-armon-go-proxyproto
Version:        0
Release:        0.4%{?dist}
Summary:        Golang package to handle HAProxy Proxy Protocol
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181112git5b7edb6
- Bump to commit 5b7edb60ff5f69b60d1950397f7bde6171f1807d
- Update to new go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170621git48572f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170621git48572f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170621git48572f1
- First package for Fedora

