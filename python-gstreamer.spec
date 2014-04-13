%define		pname	gst-python

Summary:	GStreamer Python 2 bindings
Name:		python-gstreamer
Version:	1.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.bz2
# Source0-md5:	da9a33cccdb7d094f243e4b469cfbc76
URL:		http://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	python-pygobject3-devel
BuildRequires:	python3-devel
BuildRequires:	python3-pygobject3-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python 2 bindings.

%package -n python3-gstreamer
Summary:	GStreamer Python 3 bindings
Group:		Libraries/Python
Requires:	python3-pygobject3

%description -n python3-gstreamer
GStreamer Python 3 bindings.

%prep
%setup -qn %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}

install -d python2
cd python2
../%configure \
	PYTHON="%{__python}" \
	--disable-silent-rules
%{__make}
cd ..

install -d python3
cd python3
../%configure \
	PYTHON="%{__python3}" \
	--disable-silent-rules
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C python2 install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides/*.la

%{__make} -C python3 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/gi/overrides/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{py_sitedir}/gi/overrides/_gi_gst.so
%{py_sitedir}/gi/overrides/Gst.py[co]
%{py_sitedir}/gi/overrides/GstPbutils.py[co]

%files -n python3-gstreamer
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{py3_sitedir}/gi/overrides/_gi_gst.so
%{py3_sitedir}/gi/overrides/Gst.py
%{py3_sitedir}/gi/overrides/GstPbutils.py
%{py3_sitedir}/gi/overrides/__pycache__/Gst.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstPbutils.*.py[co]

