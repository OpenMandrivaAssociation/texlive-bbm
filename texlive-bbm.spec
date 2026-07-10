%global tl_name bbm
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Blackboard-style cm fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm/bbm
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Blackboard variants of Computer Modern fonts. The fonts are distributed
as Metafont source (only); LaTeX support is available with the bbm-
macros package. The Sauter font package has Metafont parameter source
files for building the fonts at more sizes than you could reasonably
imagine. A sample of these fonts appears in the blackboard bold sampler.

