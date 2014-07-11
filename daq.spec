%define major 1
%define sfbpfmajor 0
%define libname %mklibname %{name} %{major}
%define libsfbpf %mklibname sfbpf %{sfbpfmajor}
%define devname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Summary:	Data Acquisition library, for packet I/O
Name:		daq
Version:	1.1.1
Release:	7
License:	GPLv2+
Group:		Networking/Other
Url:		http://www.snort.org/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	dnet-devel
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig(libipq)
BuildRequires:	pkgconfig(libnetfilter_queue)
BuildRequires:	pkgconfig(xtables)

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
This package contains the shared library for %{name}.

%package -n     %{libsfbpf}
Summary:        Library for DAQ
Group:          System/Libraries

%description -n %{libsfbpf}
This package contains the shared library for %{name}.

%package -n     %{name}-modules
Summary:        Bundled DAQ modules
Group:          System/Libraries
Provides:       %{name}-modules = %{EVRD}

%description -n %{name}-modules
Contains the DAQ modules that come bundled with the base LibDAQ distribution.

%package -n     %{devname}
Summary:        Development libraries and header files for DAQ
Group:          Development/C
Requires:       %{libname} = %{version}
Requires:       %{libsfbpf} = %{version}
Provides:       %{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the development libraries and header files for %{name}.

%package -n     %{staticname}
Summary:        Static libraries for DAQ
Group:          Development/C
Requires:       %{devname} = %{version}
Provides:       %{name}-static-devel = %{EVRD}

%description -n %{staticname}
This package contains the static libraries for %{name}.

%prep
%setup -q 

%build
%configure2_5x \
	--disable-static \
	--disable-ipfw-module

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

%files  -n %{devname}
%{_bindir}/daq-modules-config
%{_includedir}/*.h
%{_libdir}/*.so

%files  -n %{staticname}
%{_libdir}/*.a

