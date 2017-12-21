#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsoncpp
Version  : 1.8.4
Release  : 2
URL      : https://github.com/open-source-parsers/jsoncpp/archive/1.8.4.tar.gz
Source0  : https://github.com/open-source-parsers/jsoncpp/archive/1.8.4.tar.gz
Summary  : A C++ library for interacting with JSON
Group    : Development/Tools
License  : MIT
Requires: jsoncpp-lib
BuildRequires : cmake
BuildRequires : meson
BuildRequires : ninja
BuildRequires : python3

%description
# JsonCpp
[![badge](https://img.shields.io/badge/conan.io-jsoncpp%2F1.8.0-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/jsoncpp/1.8.0/theirix/ci)

%package dev
Summary: dev components for the jsoncpp package.
Group: Development
Requires: jsoncpp-lib
Provides: jsoncpp-devel

%description dev
dev components for the jsoncpp package.


%package lib
Summary: lib components for the jsoncpp package.
Group: Libraries

%description lib
lib components for the jsoncpp package.


%prep
%setup -q -n jsoncpp-1.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513872563
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1513872563
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/json/allocator.h
/usr/include/json/assertions.h
/usr/include/json/autolink.h
/usr/include/json/config.h
/usr/include/json/features.h
/usr/include/json/forwards.h
/usr/include/json/json.h
/usr/include/json/reader.h
/usr/include/json/value.h
/usr/include/json/version.h
/usr/include/json/writer.h
/usr/lib64/libjsoncpp.so
/usr/lib64/pkgconfig/jsoncpp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjsoncpp.so.1.8.4
/usr/lib64/libjsoncpp.so.19
