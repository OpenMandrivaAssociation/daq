%define major 3
%define libname %mklibname %{name} %{major}

%define sfbpfmajor 0
#define libsfbpf %mklibname sfbpf %{sfbpfmajor}

%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Name:		daq
Version:	3.0.13
Release:	1
Summary:	Data Acquisition library, for packet I/O
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.snort.org/
Source0:	https://github.com/snort3/libdaq/archive/refs/tags/v%{version}/libdaq-%{version}.tar.gz

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(libnetfilter_queue)
BuildRequires:	pkgconfig(libipq)
BuildRequires:          pkgconfig(libpcap)
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

#package -n %{libsfbpf}
#Summary:	Library for daq
#Group:		System/Libraries
#Conflicts:	%{_lib}daq1 < %{version}-%{release}
#Conflicts:	%{_lib}daq0 < %{version}-%{release}

#description -n %{libsfbpf}
#Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
#DAQ replaces direct calls to PCAP functions with an abstraction layer that
#facilitates operation on a variety of hardware and software interfaces without
#requiring changes to Snort.  It is possible to select the DAQ type and mode
#when invoking Snort to perform PCAP readback or inline operation, etc.  The
#DAQ library may be useful for other packet processing applications and the
#modular nature allows you to build new modules for other platforms.
#
%package modules
Summary:	Bundled DAQ modules
Group:		System/Libraries

%description modules
Contains the DAQ modules that come bundled with the base LibDAQ distribution.

%package -n %{develname}
Summary:	Header files for the dssl library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
#Requires:	%{libsfbpf} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	pkgconfig(openssl)
Requires:	pkgconfig(libpcap)
Requires:	pkgconfig(zlib)

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
%autosetup -n libdaq-%{version} -p1

%build
./bootstrap
%configure \
            --disable-ipfw-module \
            --enable-bpf-module
# Parallel builds sometimes fail unless this is built first
#make_build -C sfbpf sf_grammar.c
%make_build

%install
%make_install

%files modules
%{_libdir}/daq

%files -n %{libname}
%doc README*
%{_libdir}/libdaq.so.%{major}
%{_libdir}/libdaq.so.%{major}.*

#files -n %{libsfbpf}
#{_libdir}/libsfbpf.so.%{sfbpfmajor}
#{_libdir}/libsfbpf.so.%{sfbpfmajor}.*

%files  -n %{develname}
%{_bindir}/daqtest
%{_bindir}/daqtest-static
%{_includedir}/daq_*
%{_includedir}/daq.h
%{_libdir}/libdaq.so 
%{_libdir}/pkgconfig/libdaq.pc

%files  -n %{staticname}
%{_libdir}/libdaq_static_*
%{_libdir}/pkgconfig/libdaq_static*
