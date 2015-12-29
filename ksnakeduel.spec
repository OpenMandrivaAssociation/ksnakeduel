Name:		ksnakeduel
Version:	15.12.0
Release:	2
Epoch:		1
Summary:	Snake race played against the computer
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksnakeduel/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)
Obsoletes:	kdesnake < 1:4.9.80
Provides:	kdesnake = %{EVRD}
Provides:	ksnake = %{EVRD}
Requires:	ktron = %{EVRD}

%description
KSnakeDuel is a fast action game where you steer a snake which has to eat
food. While eating the snake grows. But once a player collides with the
other snake or the wall the game is lost. This becomes of course more and
more difficult the longer the snakes grow.

%files
%{_bindir}/ksnakeduel                                                                                    
%{_datadir}/applications/kde4/ksnakeduel.desktop   
%{_datadir}/config.kcfg/ksnakeduel.kcfg
%{_datadir}/apps/ktron/ksnakeduelui.rc
%{_datadir}/config/ksnakeduel.knsrc
%{_iconsdir}/hicolor/*/*/ksnakeduel.*    
%{_datadir}/apps/ksnakeduel/themes/*
%doc %{_docdir}/HTML/en/ksnakeduel/*
  
#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

