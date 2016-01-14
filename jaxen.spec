%global pkg_name jaxen
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.1.3
Release:        11.12%{?dist}
Epoch:          0
Summary:        An XPath engine written in Java
License:        BSD
URL:            http://jaxen.codehaus.org/
Source0:        http://dist.codehaus.org/jaxen/distributions/jaxen-%{version}-src.tar.gz
Source1:        build.xml
Source2:        http://repo1.maven.org/maven2/%{pkg_name}/%{pkg_name}/%{version}/%{pkg_name}-%{version}.pom
Requires:       %{?scl_prefix}dom4j >= 0:1.6.1
Requires:       %{?scl_prefix}jdom >= 0:1.0-0.rc1.1jpp
Requires:       %{?scl_prefix}xalan-j2
Requires:       %{?scl_prefix}xerces-j2
BuildRequires:  %{?scl_prefix}javapackages-tools
BuildRequires:  %{?scl_prefix}ant >= 0:1.6
BuildRequires:  %{?scl_prefix}junit
BuildRequires:  %{?scl_prefix}ant-junit
BuildRequires:  %{?scl_prefix}dom4j >= 0:1.6.1
BuildRequires:  %{?scl_prefix}jdom >= 0:1.0-0.rc1.1jpp
BuildRequires:  %{?scl_prefix}xalan-j2
BuildRequires:  %{?scl_prefix}xerces-j2
BuildArch:      noarch

%description
Jaxen is an XPath engine written in Java to work against a variety of XML
based object models such as DOM, dom4j and JDOM together with Java
Beans.

%package demo
Summary:        Samples for %{pkg_name}
Requires:       %{name} = 0:%{version}-%{release}

%description demo
%{summary}.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
find . -name "*.jar" -exec rm -f {} \;
cp %{SOURCE1} .
cp %{SOURCE2} pom.xml
mkdir -p target/lib
pushd target/lib
build-jar-repository . dom4j-1.6.1.jar jdom-1.0.jar 
ln -s %{_javadir}/xerces-j2.jar xercesImpl-2.6.2.jar
popd
rm -rf src/java/main/org/jaxen/xom
rm src/java/test/org/jaxen/test/XOM*.java
%pom_remove_dep xom:xom
%pom_remove_dep :maven-cobertura-plugin
%pom_remove_dep :maven-findbugs-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
mkdir .maven
export CLASSPATH=$(build-classpath xml-commons-apis)
ant -Dant.build.sysclasspath=first jar javadoc
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{pkg_name}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{pkg_name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{pkg_name}-%{version}/samples
cp -pr src/java/samples/* $RPM_BUILD_ROOT%{_datadir}/%{pkg_name}-%{version}/samples

# POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap -a saxpath:saxpath
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt

%files javadoc
%doc %{_javadocdir}/*

%files demo
%{_datadir}/%{pkg_name}-%{version}

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:1.1.3-11.12
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 0:1.1.3-11.11
- Mass rebuild 2015-01-09

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 1.1.3-11.10
- Migrate to .mfiles

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.9
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.8
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.7
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 0:1.1.3-11.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.1.3-11
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-10
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 28 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-8
- Remove xom dependency from POM
- Resolves: rhbz#880970

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-7
- Remove unneeded dependency from POM: maven-cobertura-plugin
- Remove unneeded dependency from POM: maven-findbugs-plugin
- Resolves: rhbz#880692

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-6
- Add maven POM

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Tomas Radej <tradej@redhat.com> - 0:1.1.3-4
- Removed xom dep from pom

* Mon Feb 27 2012 Tomas Radej <tradej@redhat.com> - 0:1.1.3-3
- Removed XOM support (bz #785007)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.3-1
- Update to latest upstream version.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Devrim GUNDUZ <devrim@gunduz.org> - 0:1.1.1-1
- Update to 1.1.1, to fix #465987 .

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.1-1.3
- drop repotag

* Tue Feb 20 2007 Vivek Lakshmanan <vivekl@redhat.com> 0:1.1-1jpp.2.fc7
- Add build-requires on ant-junit

* Mon Feb 19 2007 Andrew Overholt <overholt@redhat.com> 0:1.1-1jpp.1
- Add explicit version-release on Provides and Obsoletes
- Untabify
- Remove %%ghost on versioned javadoc dir
- Just include %%{_javadocdir}/* for javadoc package

* Wed Feb 14 2007 Andrew Overholt <overholt@redhat.com> 0:1.1-1jpp.1
- Bump to 1.1 final
- Make release Xjpp.Y%{?dist}
- Remove Distribution, Vendor
- Fix Group
- Remove cleaning of buildroot from beginning of %%prep
- Add cleaning of buildroot to beginning of %%install
- Remove %%section free
- Use Fedora buildroot

* Sun Feb 26 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.1-0.b7.4jpp
- Rebuild for JPP 1.7

* Wed Feb 15 2006 Ralph Apel <r.apel@r-apel.de> 0:1.1-0.b7.3jpp
- Insert Copyright notice

* Mon Feb 13 2006 Ralph Apel <r.apel@r-apel.de> 0:1.1-0.b7.2jpp
- Adapt to maven-1.1
- Create option to build without maven

* Wed Aug 17 2005 Ralph Apel <r.apel@r-apel.de> 0:1.1-0.b7.1jpp
- Upgrade to 1.1-beta-7
- Now mavenized
- Requiring dom4j >= 1.6.1
- rpmbuild option to inhibit build of manual (needs newer maven)

* Thu Sep 09 2004 Ralph Apel <r.apel@r-apel.de> 0:1.1-0.b2.1jpp
- Upgrade to 1.1-beta-2
- Drop saxpath requirement as saxpath is now included in jaxen

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0-4jpp
- Rebuild with ant-1.6.2
* Mon Jan 19 2004 Ralph Apel <r.apel@r-apel.de> 0:1.0-3jpp
- build against dom4j-1.4-1jpp
- introduce manual and demo subpackages
- patch org.jaxen.dom4j.DocumentNavigatorTest
- include LICENSE in main package
- run tests during build

* Thu Jan 15 2004 Ralph Apel <r.apel@r-apel.de> 0:1.0-2jpp
- activate support for dom4j by renaming lib/dom4j-core.jar to .zip

* Sun May 04 2003 David Walluck <david@anti-microsoft.org> 0:1.0-1jpp
- release
