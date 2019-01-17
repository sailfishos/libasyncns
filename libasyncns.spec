Name:       libasyncns
Summary:    Asynchronous Name Service Library
Version:    0.8
Release:    2
Group:      System/Libraries
License:    LGPLv2+
URL:        http://0pointer.de/lennart/projects/libasyncns
Source0:    http://0pointer.de/lennart/projects/libasyncns/libasyncns-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
libasyncns is a C library for Linux/Unix for executing name service queries asynchronously. 
It is an asynchronous wrapper around getaddrinfo(3), getnameinfo(3), res_query(3) and 
res_search(3) from libc and libresolv.

%package devel
Summary:    Development components for the libasyncns library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Devel files for the libsyncns.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static \
    --disable-rpath

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mv %{buildroot}%{_docdir}/%{name}{,-%{version}}
install -m0644 README %{buildroot}%{_docdir}/%{name}-%{version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/libasyncns.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
