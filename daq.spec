%define name    daq
%define version 0.2
%define release %mkrel 1
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

export LIBS=-lpcap 
%configure2_5x --enable-shared

%build
%make
%install
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/libdaq.so.%{major}*
%{_libdir}/libsfbpf.so.%{major}*

%files  -n %{develname}
%defattr(-,root,root)
%{_bindir}/daq-modules-config
%{_includedir}/daq.h
%{_includedir}/daq_api.h
%{_includedir}/daq_common.h
%{_includedir}/sfbpf.h
%{_includedir}/sfbpf_dlt.h
%{_libdir}/daq/daq_afpacket.la
%{_libdir}/daq/daq_afpacket.so
%{_libdir}/daq/daq_dump.la
%{_libdir}/daq/daq_dump.so
%{_libdir}/daq/daq_ipfw.la
%{_libdir}/daq/daq_ipfw.so
%{_libdir}/daq/daq_pcap.la
%{_libdir}/daq/daq_pcap.so
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


