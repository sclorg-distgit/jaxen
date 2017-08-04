%{?scl:%scl_package jaxen}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}jaxen
Epoch:          0
Version:        1.1.6
Release:        11.2%{?dist}
Summary:        An XPath engine written in Java
License:        BSD
URL:            http://jaxen.codehaus.org/
BuildArch:      noarch

Source0:        http://dist.codehaus.org/jaxen/distributions/%{pkg_name}-%{version}-src.tar.gz

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(dom4j:dom4j)
BuildRequires:  %{?scl_prefix}mvn(jdom:jdom)
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(xerces:xercesImpl)
BuildRequires:  %{?scl_prefix}mvn(xml-apis:xml-apis)

%description
Jaxen is an open source XPath library written in Java. It is adaptable
to many different object models, including DOM, XOM, dom4j, and JDOM.
Is it also possible to write adapters that treat non-XML trees such as compiled
Java byte code or Java beans as XML, thus enabling you to query these trees
with XPath too.

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
%setup -n %{pkg_name}-%{version} -q 

rm -rf src/java/main/org/jaxen/xom
rm src/java/test/org/jaxen/test/XOM*.java
%pom_remove_dep xom:xom

%mvn_file : %{pkg_name}

%build
%mvn_build -f

%install
%mvn_install

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{pkg_name}/samples
cp -pr src/java/samples/* %{buildroot}%{_datadir}/%{pkg_name}/samples

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files demo
%{_datadir}/%{pkg_name}

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 0:1.1.6-11.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 0:1.1.6-11.1
- Automated package import and SCL-ization

* Tue Mar  7 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.6-11
- Don't hardcode package name

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.6-9
- Add missing build-requires
- Remove old obsoletes/provides

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Michal Srb <msrb@redhat.com> - 0:1.1.6-6
- Rebuild to regenerate R

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.6-5
- Fix build-requires on sonatype-oss-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1.6-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Jan 29 2014 Michal Srb <msrb@redhat.com> - 0:1.1.6-2
- Remove saxpath provides (Resolves: rhbz#1059229)

* Mon Sep 02 2013 Michal Srb <msrb@redhat.com> - 0:1.1.6-1
- Update to upstream version 1.1.6
- Build with Maven
- Update description
- Adapt to current guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
