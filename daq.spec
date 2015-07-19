%define major 2
%define libname %mklibname %{name} %{major}

%define sfbpfmajor 0
%define libsfbpf %mklibname sfbpf %{sfbpfmajor}

%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Name:		daq
Version:	2.0.2
Release:	3
Summary:	Data Acquisition library, for packet I/O
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.snort.org/
Source0:	http://www.snort.org/downloads/%{name}-%{version}.tar.gz
Source1:	http://www.snort.org/downloads/%{name}-%{version}.tar.gz.sig
BuildRequires:	pcap-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(libnetfilter_queue)
BuildRequires:	pkgconfig(libipq)
BuildRequires:	pkgconfig(xtables)
BuildRequires:	dnet-devel

%description
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package -n %{libname}
Summary:	Main library for daq
Group:		System/Libraries

%description -n %{libname}
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package -n %{libsfbpf}
Summary:	Library for daq
Group:		System/Libraries
Conflicts:	%{_lib}daq1 < %{version}-%{release}
Conflicts:	%{_lib}daq0 < %{version}-%{release}

%description -n %{libsfbpf}
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package modules
Summary:	Bundled DAQ modules
Group:		System/Libraries

%description modules
Contains the DAQ modules that come bundled with the base LibDAQ distribution.

%package -n %{develname}
Summary:	Header files for the dssl library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libsfbpf} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	openssl-devel
Requires:	libpcap-devel
Requires:	zlib-devel

%description -n %{develname}
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package -n     %{staticname}
Summary:        Static libraries for DAQ
Group:          Development/C
Requires:       %{develname} = %{version}
Provides:       %{name}-static-devel = %{EVRD}

%description -n %{staticname}
This package contains the static libraries for %{name}.

%prep
%setup -q

%build
%configure --disable-ipfw-module
# Parallel builds sometimes fail unless this is built first
%make -C sfbpf sf_grammar.c
%make

%install
%makeinstall_std

%files modules
%{_libdir}/daq

%files -n %{libname}
%doc README
%{_libdir}/libdaq.so.%{major}
%{_libdir}/libdaq.so.%{major}.*

%files -n %{libsfbpf}
%{_libdir}/libsfbpf.so.%{sfbpfmajor}
%{_libdir}/libsfbpf.so.%{sfbpfmajor}.*

%files  -n %{develname}
%{_bindir}/daq-modules-config
%{_includedir}/daq.h
%{_includedir}/daq_api.h
%{_includedir}/daq_common.h
%{_includedir}/sfbpf.h
%{_includedir}/sfbpf_dlt.h
%{_libdir}/libdaq_static_modules.a
%{_libdir}/libsfbpf.so
%{_libdir}/libdaq.so

%files  -n %{staticname}
%{_libdir}/libdaq_static.a
