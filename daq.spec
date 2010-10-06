%define name    daq
%define version 0.2
%define release %mkrel 2
%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Data Acquisition library, for packet I/O
License:    GPLv2+
Group:      Networking/Other
URL:        http://www.snort.org/
Source:     http://www.snort.org/downloads/%{name}-%{version}.tar.gz
BuildRequires:	pcap-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:	netfilter_queue-devel
BuildRequires:	dnet-devel
BuildRequires:	iptables-ipq-devel
BuildRequires:	iptables-devel
%if %mdkversion < 200800
BuildRoot:  %{_tmppath}/%{name}-%{version}
%endif

%description
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package -n     %{libname}
Summary:        Main library for daq
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package -n     %{name}-modules
Summary:        Bundled DAQ modules
Group:          System/Libraries
Provides:       %{name}-modules = %{version}-%{release}

%description -n %{name}-modules
Contains the DAQ modules that come bundled with the base LibDAQ distribution.

%package        -n     %{develname}
Summary:        Header files for the dssl library
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Requires:  openssl-devel
Requires:  libpcap-devel
Requires:  zlib-devel

%description    -n %{develname}
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

These are .h files.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%prep
%setup -q 

%configure2_5x --disable-ipfw-module

%build
%make
%install
%makeinstall_std
# Remove the .la files for the DAQ modules -- we don't want them!
%{__rm} -f %{buildroot}/%{_libdir}/daq/*.la

%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/libdaq.so.%{major}*
%{_libdir}/libsfbpf.so.%{major}*

%files -n %{name}-modules
%defattr(-,root,root)
%{_libdir}/daq/daq_afpacket.so
%{_libdir}/daq/daq_dump.so
%{_libdir}/daq/daq_ipq.so
%{_libdir}/daq/daq_nfq.so
%{_libdir}/daq/daq_pcap.so

%files  -n %{develname}
%defattr(-,root,root)
%{_bindir}/daq-modules-config
%{_includedir}/daq.h
%{_includedir}/daq_api.h
%{_includedir}/daq_common.h
%{_includedir}/sfbpf.h
%{_includedir}/sfbpf_dlt.h
%{_libdir}/libdaq_static.a
%{_libdir}/libdaq_static.la
%{_libdir}/libdaq_static_modules.a
%{_libdir}/libdaq_static_modules.la
%{_libdir}/libsfbpf.a
%{_libdir}/libsfbpf.la
%{_libdir}/libsfbpf.so

%{_libdir}/libdaq.so
%{_libdir}/libdaq.a
%{_libdir}/libdaq.la


