%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-moveit-python
Version:        0.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_python package

License:        BSD
URL:            http://ros.org/wiki/moveit_python
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-assimp
Requires:       ros-noetic-actionlib
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-moveit-msgs
Requires:       ros-noetic-rospy
Requires:       ros-noetic-shape-msgs
Requires:       ros-noetic-tf
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A pure-python interaface to the MoveIt! ROS API.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sun Jan 17 2021 Michael Ferguson <fergs@botnuvo.com> - 0.4.0-1
- Autogenerated by Bloom

* Sun Jan 17 2021 Michael Ferguson <fergs@botnuvo.com> - 0.3.6-2
- Autogenerated by Bloom

* Fri Dec 25 2020 Michael Ferguson <fergs@botnuvo.com> - 0.3.6-1
- Autogenerated by Bloom

