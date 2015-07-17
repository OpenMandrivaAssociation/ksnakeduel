Name:		ksnakeduel
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Snake race played against the computer
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksnakeduel/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-level
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
%{_bindir}/kdesnake                                                                                    
%{_datadir}/applications/kde4/kdesnake.desktop                                                         
%{_iconsdir}/hicolor/*/*/kdesnake.*                                                                    
  
#------------------------------------------------------------------------------

%package -n ktron
Summary:	Simple Tron clone
Group:		Graphical desktop/KDE
URL:		http://www.kde.org/applications/games/ktron

%description -n ktron
Well known from the famous movie, KTron is a popular computer game for two
players. In a fast action sequence both players have to move and avoid
colliding with any walls, the opponent as well as the own path. The player
colliding first looses the game.

%files -n ktron
%{_bindir}/ktron                                                                                       
%{_datadir}/applications/kde4/ktron.desktop                                                            
%{_datadir}/apps/ktron                                                                                 
%{_datadir}/config.kcfg/ktron.kcfg                                                                     
%{_datadir}/config/ktron.knsrc                                                                         
%{_iconsdir}/hicolor/*/*/ktron.png                                                                     
%doc %{_docdir}/HTML/en/ktron   

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

