#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-felix
Version  : 1.0.0
Release  : 6
URL      : https://repo1.maven.org/maven2/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.jar
Source0  : https://repo1.maven.org/maven2/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.jar
Source1  : https://repo1.maven.org/maven2/org/apache/felix/felix-parent/1.2.1/felix-parent-1.2.1.pom
Source2  : https://repo1.maven.org/maven2/org/apache/felix/felix-parent/2.1/felix-parent-2.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/felix/felix-parent/3/felix-parent-3.pom
Source4  : https://repo1.maven.org/maven2/org/apache/felix/felix-parent/4/felix-parent-4.pom
Source5  : https://repo1.maven.org/maven2/org/apache/felix/felix/1.0.0/felix-1.0.0.pom
Source6  : https://repo1.maven.org/maven2/org/apache/felix/felix/1.0.2/felix-1.0.2.pom
Source7  : https://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.utils/1.6.0/org.apache.felix.utils-1.6.0.jar
Source8  : https://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.utils/1.6.0/org.apache.felix.utils-1.6.0.pom
Source9  : https://repo1.maven.org/maven2/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.jar
Source10  : https://repo1.maven.org/maven2/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.pom
Source11  : https://repo1.maven.org/maven2/org/apache/felix/org.osgi.service.obr/1.0.1/org.osgi.service.obr-1.0.1.jar
Source12  : https://repo1.maven.org/maven2/org/apache/felix/org.osgi.service.obr/1.0.1/org.osgi.service.obr-1.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-felix-data = %{version}-%{release}
Requires: mvn-felix-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-felix package.
Group: Data

%description data
data components for the mvn-felix package.


%package license
Summary: license components for the mvn-felix package.
Group: Default

%description license
license components for the mvn-felix package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-felix
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-felix/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/1.2.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/1.2.1/felix-parent-1.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/2.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/2.1/felix-parent-2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/3/felix-parent-3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/4
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix-parent/4/felix-parent-4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix/1.0.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix/1.0.0/felix-1.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix/1.0.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/felix/1.0.2/felix-1.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.apache.felix.utils/1.6.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.apache.felix.utils/1.6.0/org.apache.felix.utils-1.6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.apache.felix.utils/1.6.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.apache.felix.utils/1.6.0/org.apache.felix.utils-1.6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.service.obr/1.0.1
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.service.obr/1.0.1/org.osgi.service.obr-1.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.service.obr/1.0.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/felix/org.osgi.service.obr/1.0.1/org.osgi.service.obr-1.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/felix/felix-parent/1.2.1/felix-parent-1.2.1.pom
/usr/share/java/.m2/repository/org/apache/felix/felix-parent/2.1/felix-parent-2.1.pom
/usr/share/java/.m2/repository/org/apache/felix/felix-parent/3/felix-parent-3.pom
/usr/share/java/.m2/repository/org/apache/felix/felix-parent/4/felix-parent-4.pom
/usr/share/java/.m2/repository/org/apache/felix/felix/1.0.0/felix-1.0.0.pom
/usr/share/java/.m2/repository/org/apache/felix/felix/1.0.2/felix-1.0.2.pom
/usr/share/java/.m2/repository/org/apache/felix/org.apache.felix.utils/1.6.0/org.apache.felix.utils-1.6.0.jar
/usr/share/java/.m2/repository/org/apache/felix/org.apache.felix.utils/1.6.0/org.apache.felix.utils-1.6.0.pom
/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.jar
/usr/share/java/.m2/repository/org/apache/felix/org.osgi.core/1.0.0/org.osgi.core-1.0.0.pom
/usr/share/java/.m2/repository/org/apache/felix/org.osgi.service.obr/1.0.1/org.osgi.service.obr-1.0.1.jar
/usr/share/java/.m2/repository/org/apache/felix/org.osgi.service.obr/1.0.1/org.osgi.service.obr-1.0.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-felix/LICENSE
