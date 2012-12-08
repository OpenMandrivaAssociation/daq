%define major 1
%define sfbpfmajor 0
%define libname %mklibname %{name} %{major}
%define libsfbpf %mklibname sfbpf %{sfbpfmajor}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Name:		daq
Version:	1.1.1
Release:	1
Summary:	Data Acquisition library, for packet I/O
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.snort.org/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	pcap-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:	netfilter_queue-devel
BuildRequires:	dnet-devel
BuildRequires:	iptables-ipq-devel
BuildRequires:	iptables-devel

%description
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package -n     %{libname}
Summary:        Main library for DAQ
Group:          System/Libraries
Provides:       %{name} = %{EVRD}

%description -n %{libname}
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package -n     %{libsfbpf}
Summary:        Library for DAQ
Group:          System/Libraries

%description -n %{libsfbpf}
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
Provides:       %{name}-modules = %{EVRD}

%description -n %{name}-modules
Contains the DAQ modules that come bundled with the base LibDAQ distribution.

%package -n     %{develname}
Summary:        Development libraries and header files for DAQ
Group:          Development/C
Requires:       %{libname} = %{version}
Requires:       %{libsfbpf} = %{version}
Provides:       %{name}-devel = %{EVRD}

%description -n %{develname}
This package contains the development libraries and header files for %{name}.

%package -n     %{staticname}
Summary:        Static libraries for DAQ
Group:          Development/C
Requires:       %{develname} = %{version}
Provides:       %{name}-static-devel = %{EVRD}

%description -n %{staticname}
This package contains the static libraries for %{name}.

%prep
%setup -q 

%configure2_5x \
	--disable-static \
	--disable-ipfw-module

%build
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdaq.so.%{major}*

%files -n %{libsfbpf}
%{_libdir}/libsfbpf.so.%{sfbpfmajor}*

%files -n %{name}-modules
%doc README
%{_libdir}/daq/daq_afpacket.so
%{_libdir}/daq/daq_dump.so
#%{_libdir}/daq/daq_ipq.so
%{_libdir}/daq/daq_nfq.so
%{_libdir}/daq/daq_pcap.so

%files  -n %{develname}
%{_bindir}/daq-modules-config
%{_includedir}/*.h
%{_libdir}/*.so

%files  -n %{staticname}
%{_libdir}/*.a
