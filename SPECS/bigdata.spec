Name:          bigdata
Version:       1.0 
Release:       1%{?dist}
Summary:       install hadoop

License:       Shareware
#URL:            
#Source0:        %{_sourcedir}/Release/hadoop-2.7.3.tar.gz
#Source1:	 %{_sourcedir}/Release/spark-2.1.0-bin-hadoop2.7.tgz
#Source2:	 %{_sourcedir}/Release/zookeeper-3.4.9.tar.gz
#Source3:	install.sh

#BuildRequires:  
#Requires:       

%description
autoinstall hadoop

%prep
#cd $RPM_BUILD_DIR
#%setup -b -n 0 %{_builddir}/hadoop
#%setup -b -n 1 %{_builddir}/spark
#%setup -b -n 2 %{_builddir}/zookeeper 
#cp %{_sourcedir}/install.sh %{_builddir}/%{name}-%{version}/
#cp %{_sourcedir}/install.sh %{_buildrootdir}/%{name}-%{version}-%{release}/


%build


%install
cd %{_sourcedir}
#install %{_sourcedir}/install.sh %{_builddir}/%{name}-%{version}/
install -d %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/bigdata 
scp -r  %{_sourcedir}/* %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/bigdata 
#install  %{_sourcedir}/process.sh %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/bigdata/ 
#install  %{_sourcedir}/install.sh %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/bigdata/ 
#install  %{_sourcedir}/updatexml.py %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/bigdata/ 
#install  %{_sourcedir}/conf.xml %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/bigdata/ 
#install  %{_sourcedir}/config.properties %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/bigdata/ 
#cp -r %{_sourcedir}/conf/ %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/bigdata/ 
#install  %{SOURCE0} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}/run/new/bigdata/ 
#cp %{_sourcedir}/install.sh %{_buildrootdir}/%{name}-%{version}-%{_arch}/
#rm -rf $RPM_BUILD_ROOT
#%make_install


%files 
%defattr(-, root, root, -)
/bigdata/*



%post
exec 6<&0 0</dev/tty
cd /bigdata/ 

sh prepare.sh
exec 0<&6 6<&-
sh install.sh install
sh install.sh startup

#rm -rf /bigdata/ 

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if[ -d "/bigdata" ] ; then
 cd /bigdata 
 if[ -d "userconf.properties" ] ; then
  sh install.sh stop
  sh install.sh uninstall
 else
  rm -rf /bigdata 
 fi
fi



%changelog
