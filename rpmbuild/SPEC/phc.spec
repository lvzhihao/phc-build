svn_url git://github.com/lvzhihao/phc-build.git
%define rev 0.1

Name:           phc
Version:        r%{rev}
Release:        r3415
Summary:        phc

Group:          Development/Languages
License:        ERPL
URL:            http://www.shopex.cn
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  m4
BuildRequires:  libtool
BuildRequires:  libicu-devel
BUildRequires:  libxml2-devel
BUildRequires:  mysql >= 4
BUildRequires:  git

Requires:  mysql >= 4

%description
phc for php5.3.x

%prep
export LC_ALL=en_US.UTF-8
git clone git://github.com/lvzhihao/phc-build.git phc

%build
cd phc
./configure --prefix=/usr/local/phc
DESTDIR=$RPM_BUILD_ROOT make

%install
rm -rf $RPM_BUILD_ROOT
cd phc/pkgs/phc
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT rpmbuildfix
mkdir -p $RPM_BUILD_ROOT/usr/bin
ln -sf /usr/local/phc/bin/phc $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/phc
/usr/bin
