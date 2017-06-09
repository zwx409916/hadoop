Name:          hadoop
Version:        2.7.3
Release:        1%{?dist}
Summary:        install hadoop

License:        Shareware
#URL:            
Source0:        %{_sourcedir}/Release/hadoop-2.7.3.tar.gz
Source1:	 %{_sourcedir}/Release/spark-2.1.0-bin-hadoop2.7.tgz
Source2:	 %{_sourcedir}/Release/zookeeper-3.4.9.tar.gz
Source3:	install.sh

#BuildRequires:  
#Requires:       

%description
autoinstall hadoop

%prep
#%setup -q
#%setup -n hadoop
#%setup -n spark
#%setup -n zookeeper
#cd $RPM_BUILD_DIR
#%setup -b -n 0 %{_builddir}/hadoop
#%setup -b -n 1 %{_builddir}/spark
#%setup -b -n 2 %{_builddir}/zookeeper 
#tar -zxvf %{SOURCE1}
#%setup -q %{SOURCE2}
#cp %{_sourcedir}/install.sh %{_builddir}/%{name}-%{version}/
#cp %{_sourcedir}/install.sh %{_buildrootdir}/%{name}-%{version}-%{release}/



%build
#./configure
${_builddir}
 
#make %{?_smp_mflags}


%install
cd %{_sourcedir}
#install %{_sourcedir}/install.sh %{_builddir}/%{name}-%{version}/
install -d %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
scp -r  %{_sourcedir}/* %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#install  %{_sourcedir}/process.sh %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#install  %{_sourcedir}/install.sh %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#install  %{_sourcedir}/updatexml.py %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#install  %{_sourcedir}/conf.xml %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#install  %{_sourcedir}/config.properties %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#cp -r %{_sourcedir}/conf/ %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#install  %{SOURCE0} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/cache
#cp %{_sourcedir}/install.sh %{_buildrootdir}/%{name}-%{version}-%{_arch}/
#rm -rf $RPM_BUILD_ROOT
#%make_install


%files 
%defattr(-, root, root, -)
#/install.sh
#/process.sh
#/updatexml.py
#/updatexml.pyc
#/updatexml.pyo
#/conf.xml
#/conf/
/run/new/cache/*
#/install.sh


%post
echo `pwd`
cd /run/new/cache/
echo `pwd`
sh install.sh install
echo `pwd`
sh install.sh startup


%changelog
