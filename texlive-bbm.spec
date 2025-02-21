Name:		texlive-bbm
Version:	15878
Release:	2
Summary:	"Blackboard-style" cm fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm/bbm
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Blackboard variants of Computer Modern fonts. The fonts are
distributed as MetaFont source (only); LaTeX support is
available with the bbm-macros package. The Sauter font package
has MetaFont parameter source files for building the fonts at
more sizes than you could reasonably imagine. A sample of these
fonts appears in the blackboard bold sampler.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/bbm/bbm10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm17.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm5.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm6.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm7.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmb10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx5.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx6.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx7.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbxsl10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmdunh10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmfib8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmfxib8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbminch.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsltt10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss17.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssbx10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssdc10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi17.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssq8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssqi8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmvtt10.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbbase.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbord.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbordl.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbordsp.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbordu.mf
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm5.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm6.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm7.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmdunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmfxib8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt9.tfm
%doc %{_texmfdistdir}/doc/fonts/bbm/README
%doc %{_texmfdistdir}/doc/fonts/bbm/gfbatch.batch
%doc %{_texmfdistdir}/doc/fonts/bbm/mfbatch.batch
%doc %{_texmfdistdir}/doc/fonts/bbm/test.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
