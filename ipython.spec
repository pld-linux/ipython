# NOTE: Python3 version in 'ipython3.spec'
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation (disable for bootstrap)
%bcond_with	tests	# unit tests (need to wait for fulfilling dependencies in PLD)

Summary:	An enhanced Interactive Python shell
Summary(pl.UTF-8):	Interaktywna powłoka języka Python
Name:		ipython
Version:	5.10.0
Release:	2
License:	BSD
Group:		Applications/Shells
Source0:	http://archive.ipython.org/release/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	eae7393ed47415709df3823422571a49
Patch0:		%{name}-use-setuptools.patch
URL:		http://ipython.org/
BuildRequires:	pydoc >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-devel-tools >= 1:2.7
BuildRequires:	python-modules-sqlite >= 1:2.7
BuildRequires:	python-setuptools >= 18.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.747
%if %{with tests}
BuildRequires:	python-backports.shutil_get_terminal_size
BuildRequires:	python-decorator
BuildRequires:	python-ipykernel
BuildRequires:	python-mock
BuildRequires:	python-nbformat
BuildRequires:	python-nose >= 0.10.1
BuildRequires:	python-pathlib2
BuildRequires:	python-pexpect
BuildRequires:	python-pickleshare
BuildRequires:	python-prompt_toolkit >= 1.0.4
BuildRequires:	python-prompt_toolkit < 2
BuildRequires:	python-pygments < 2.6
BuildRequires:	python-requests
BuildRequires:	python-simplegeneric >= 0.8
BuildRequires:	python-testpath
BuildRequires:	python-traitlets >= 4.2
%endif
%if %{with doc}
BuildRequires:	python-docutils
BuildRequires:	python-ipykernel
BuildRequires:	python-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-2 >= 1.3
%endif
Requires:	python-%{name} = %{version}-%{release}
Suggests:	python-PyQt5
Suggests:	python-zmq
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

%description -l pl.UTF-8
IPython jest wolnym oprogramowaniem, którego celem jest:

1. Dostarczenie interaktywnej powłoki lepszej od standardowej
dostarczanej z językiem Python. IPython umożliwia badanie obiektów,
dostęp do powłoki oraz własny system poleceń, który umożliwia
rozszerzanie funkcjonalności podczas pracy interaktywnej.

2. Dostarczenie gotowego interpretera, który można dołączać do własnej
aplikacji. IPython może zostać uruchomiony za pomocą wywołania jednej
funkcji z poziomu innego programu umożliwiając jednocześnie dostęp do
aktualnej przestrzeni nazw tego programu. Może to być bardzo użyteczne
do celów takich jak śledzenie programu czy też sytuacji gdzie jest
wymagane połączenie przetwarzania wsadowego z interaktywną
introspekcją.

3. Dostarczenie szkieletu, który może zostać użyty jako podstawa
systemu, którego polecenia opierają się na zasadach języka Python.
Projekt został zainspirowany przez oprogramowanie naukowe takie jak
Mathematica, IDL oraz Mathcad, gdzie podobne idee mogą być realizowane
w wielu przypadkach.

Pakiet ten zawiera powłokę IPython.

%package -n python-ipython
Summary:	An enhanced Interactive Python shell modules
Summary(pl.UTF-8):	Moduły interaktywnej powłoki języka Python
Group:		Libraries/Python
Requires:	pydoc >= 1:2.7
Requires:	python-devel-tools >= 1:2.7

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

%description -n python-ipython -l pl.UTF-8
IPython jest wolnym oprogramowaniem, którego celem jest:

1. Dostarczenie interaktywnej powłoki lepszej od standardowej
dostarczanej z językiem Python. IPython umożliwia badanie obiektów,
dostęp do powłoki oraz własny system poleceń, który umożliwia
rozszerzanie funkcjonalności podczas pracy interaktywnej.

2. Dostarczenie gotowego interpretera, który można dołączać do własnej
aplikacji. IPython może zostać uruchomiony za pomocą wywołania jednej
funkcji z poziomu innego programu umożliwiając jednocześnie dostęp do
aktualnej przestrzeni nazw tego programu. Może to być bardzo użyteczne
do celów takich jak śledzenie programu czy też sytuacji gdzie jest
wymagane połączenie przetwarzania wsadowego z interaktywną
introspekcją.

3. Dostarczenie szkieletu, który może zostać użyty jako podstawa
systemu, którego polecenia opierają się na zasadach języka Python.
Projekt został zainspirowany przez oprogramowanie naukowe takie jak
Mathematica, IDL oraz Mathcad, gdzie podobne idee mogą być realizowane
w wielu przypadkach.

Pakiet ten zawiera moduły interaktywnej powłoki języka Python.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	examples/Embedding/embed_class_long.py \
	"examples/IPython Kernel/ipython-get-history.py" \
	"examples/IPython Kernel/gui"/gui-*.py

%build
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTHONPATH=$(pwd) \
%{__python} IPython/testing/iptest.py IPython
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	PYTHON=%{__python} \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

# test suite
%{__rm} $RPM_BUILD_ROOT%{_bindir}/iptest*
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/IPython/{core/tests,extensions/tests,lib/tests,terminal/tests,testing/tests,utils/tests}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipython
%attr(755,root,root) %{_bindir}/ipython2
%{_mandir}/man1/ipython.1*

%files -n python-ipython
%defattr(644,root,root,755)
%doc COPYING.rst README.rst
%{py_sitescriptdir}/IPython
%{py_sitescriptdir}/ipython-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
