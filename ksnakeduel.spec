Name:		ksnakeduel
Version:	4.11.1
Release:	1
Epoch:		1
Summary:	Snake race played against the computer
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksnakeduel/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
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
%{_kde_bindir}/kdesnake
%{_kde_applicationsdir}/kdesnake.desktop
%{_kde_iconsdir}/hicolor/*/*/kdesnake.*

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
%{_kde_bindir}/ktron
%{_kde_applicationsdir}/ktron.desktop
%{_kde_appsdir}/ktron
%{_kde_datadir}/config.kcfg/ktron.kcfg
%{_kde_configdir}/ktron.knsrc
%{_kde_iconsdir}/hicolor/*/*/ktron.png
%{_kde_docdir}/HTML/en/ktron

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package


