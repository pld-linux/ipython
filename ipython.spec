%include	/usr/lib/rpm/macros.python

%define pname IPython

Summary:	An enhanced Interactive Python shell
Summary(pl):	Interaktywna pow�oka j�zyka Python
Name:		ipython
Version:	0.2.10
Release:	1
License:	LGPL
Group:		Applications/Shells
Source0:	http://www-hep.colorado.edu/~fperez/ipython/dist/%{pname}-%{version}.tar.gz
URL:		http://www-hep.colorado.edu/~fperez/ipython/
%pyrequires_eq	python
Requires:	python-%{name} = %{version}
BuildRequires:	rpm-pythonprov >= 4.0.2-50
BuildRequires:  python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPython is a free software project which tries to:

1. Provide an interactive interpreter superior to Python's default.
IPython has many features for object introspection, shell access, and
its own special command system for adding functionality when working
interactively.

2. Serve as an embeddable, ready to use interpreter for your own
programs. IPython can be started with a single call from inside
another program, providing access to the current namespace. This can
be very useful both for debugging purposes and for situations where a
blend of batch-processing and interactive exploration are needed.

3. Offer a flexible framework which can be used as the base
environment for other systems with Python as the underlying language.
Specifically scientific environments like Mathematica, IDL and Mathcad
inspired its design, but similar ideas can be useful in many fields.

This package contains IPython shell.

%description -l pl
IPython jest wolnym oprogramowaniem, kt�rego celem jest:

1. Dostarczenie interaktywnej pow�oki lepszej od standardowej
dostarczanej z j�zykiem Python. IPython umo�liwia badanie obiekt�w,
dost�p do pow�oki oraz w�asny system polece�, kt�ry umo�liwia
rozszerzanie funkcjonalno�ci podczas pracy interaktywnej.

2. Dostarczenie gotowego interpertera, kt�ry mo�na do��cza� do w�asnej
aplikacji. IPython mo�e zosta� uruchomiony za pomoc� wywo�ania jednej
funkcji z poziomu innego programu umo�liwiaj�c jednocze�nie dost�p do
aktualnej przestrzeni nazw tego programu. Mo�e to by� bardzo u�yteczne
do cel�w takich jak �ledzenie programu czy te� sytuacji gdzie jest
wymagane po��czenie przetwarzania wsadowego z interaktywn�
introspekcj�.

3. Dostarczenie szkieletu, kt�ry mo�e zosta� u�yty jako podstawa
systemu, kt�rego polecenia opieraj� si� na zasadach j�zyka Python.
Projekt zosta� zainspirowany przez oprogramowanie naukowe takie jak
Mathematica, IDL oraz Mathcad, gdzie podobne idee mog� by� realizowane
w wielu przypadkach.

Pakiet ten zawiera pow�ok� IPython.

%package -n python-ipython
Summary:	An enhanced Interactive Python shell modules
Summary(pl):	Modu�y interaktywnej pow�oki j�zyka Python
Group:		Libraries/Python
%pyrequires_eq	python-modules
%pyrequires_eq	python-pydoc

%description -n python-ipython
IPython is a free software project which tries to:

1. Provide an interactive interpreter superior to Python's default.
IPython has many features for object introspection, shell access, and
its own special command system for adding functionality when working
interactively.

2. Serve as an embeddable, ready to use interpreter for your own
programs. IPython can be started with a single call from inside
another program, providing access to the current namespace. This can
be very useful both for debugging purposes and for situations where a
blend of batch-processing and interactive exploration are needed.

3. Offer a flexible framework which can be used as the base
environment for other systems with Python as the underlying language.
Specifically scientific environments like Mathematica, IDL and Mathcad
inspired its design, but similar ideas can be useful in many fields.

This package contains IPython modules.

%description -n python-ipython -l pl
IPython jest wolnym oprogramowaniem, kt�rego celem jest:

1. Dostarczenie interaktywnej pow�oki lepszej od standardowej
dostarczanej z j�zykiem Python. IPython umo�liwia badanie obiekt�w,
dost�p do pow�oki oraz w�asny system polece�, kt�ry umo�liwia
rozszerzanie funkcjonalno�ci podczas pracy interaktywnej.

2. Dostarczenie gotowego interpertera, kt�ry mo�na do��cza� do w�asnej
aplikacji. IPython mo�e zosta� uruchomiony za pomoc� wywo�ania jednej
funkcji z poziomu innego programu umo�liwiaj�c jednocze�nie dost�p do
aktualnej przestrzeni nazw tego programu. Mo�e to by� bardzo u�yteczne
do cel�w takich jak �ledzenie programu czy te� sytuacji gdzie jest
wymagane po��czenie przetwarzania wsadowego z interaktywn�
introspekcj�.

3. Dostarczenie szkieletu, kt�ry mo�e zosta� u�yty jako podstawa
systemu, kt�rego polecenia opieraj� si� na zasadach j�zyka Python.
Projekt zosta� zainspirowany przez oprogramowanie naukowe takie jak
Mathematica, IDL oraz Mathcad, gdzie podobne idee mog� by� realizowane
w wielu przypadkach.

Pakiet ten zawiera modu�y interaktywnej pow�oki j�zyka Python.

%prep
%setup  -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

mv doc/manual/manual.pdf doc/
mv doc/manual/ doc/html/

gzip -9nf *.txt doc/{*.txt,ChangeLog,ToDo,BUGS}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files -n python-ipython
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/html doc/*.pdf
%dir %{py_sitedir}/%{pname}
%dir %{py_sitedir}/%{pname}/Extensions
%dir %{py_sitedir}/%{pname}/UserConfig
%{py_sitedir}/%{pname}/*.py?
%{py_sitedir}/%{pname}/Extensions/*.py?

# leave it as source because files below will be installed in ~/.ipython
# when IPython is _imported_ (it is the reason why UserConfig is not in
# main package) first time
%{py_sitedir}/%{pname}/UserConfig/*.py
