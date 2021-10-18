# 
# Do not Edit! Generated by:
# spectacle version 0.13~pre
# 
# >> macros
# << macros

Name:       pth
Summary:    The GNU Portable Threads library
Version:    2.0.7
Release:    6
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gnu.org/software/pth/
Source0:    ftp://ftp.gnu.org/gnu/pth/pth-%{version}.tar.gz
Source1:    ftp://ftp.gnu.org/gnu/pth/pth-%{version}.tar.gz.sig
Source100:  pth.yaml
Patch0:     pth-2.0.7-dont-remove-gcc-g.patch
Patch1:     pth-2.0.7-fixbuildlinux.patch
Patch2:     pth-2.0.7-dont-call-sigprocmask-on-pth-current.patch
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.



%package devel
Summary:    Development headers and libraries for GNU Pth
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development headers and libraries for GNU Pth.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

# >> build post
%configure --disable-static ac_cv_func_sigstack='no'


# this is necessary; without it make -j fails
make pth_p.h
make %{?_smp_mflags}



# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
# Please write install script under ">> install post"

# >> install post
%make_install
# << install post

%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
# >> files
%doc COPYING README
%{_libdir}/*.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc HACKING
%doc ANNOUNCE AUTHORS COPYING ChangeLog HISTORY NEWS PORTING README
%doc SUPPORT TESTS THANKS USERS
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/*/*
%{_datadir}/aclocal/*
# << files devel

