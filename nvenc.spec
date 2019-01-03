Name:           nvenc
Version:        8.2.16
Release:        1%{?dist}
Epoch:          1
Summary:        A comprehensive set of APIs for hardware accelerated video encode and decode
License:        https://developer.nvidia.com/nvidia-video-codec-sdk-license-agreement
URL:            https://developer.nvidia.com/nvidia-video-codec-sdk

Source0:        Video_Codec_SDK_%{version}.zip

BuildArch:      noarch

Conflicts:      nvidia-video-codec-sdk

# Required for:
# - libnvcuvid.so (NVDECODE)
# - libnvidia-encode.so (NVENCODE)
Requires:       nvidia-driver-devel >= 2:396.24
Requires:       cuda-devel >= 1:8.0

%description
The SDK consists of two hardware acceleration interfaces:

    NVENCODE API for video encode acceleration
    NVDECODE API for video decode acceleration

NVIDIA GPUs contain one or more hardware-based decoder and encoder(s) (separate
from the CUDA cores) which provides fully-accelerated hardware-based video
decoding and encoding for several popular codecs. With decoding/encoding
offloaded, the graphics engine and the CPU are free for other operations.

GPU hardware accelerator engine for video decoding (referred to as NVDEC)
supports faster than real-time decoding which makes it suitable to be used
for transcoding applications, in addition to video playback applications.

%package samples
Summary:        nvEncoder Sample application source code
Requires:       %{name} = %{?epoch}:%{version}-%{release}

%description samples
This package contains sample application source code demonstrating various
encoding and decoding capabilities.

%prep
%setup -q -n Video_Codec_SDK_%{version}
# Remove stub libraries
rm -fr Samples/NvCodec/Lib

%install
mkdir -p %{buildroot}%{_includedir}/%{name}/
install -m 644 -p \
    Samples/NvCodec/NvDecoder/cuviddec.h \
    Samples/NvCodec/NvDecoder/nvcuvid.h \
    Samples/NvCodec/NvDecoder/NvDecoder.h \
    Samples/NvCodec/NvEncoder/nvEncodeAPI.h \
    Samples/NvCodec/NvEncoder/NvEncoderCuda.h \
    Samples/NvCodec/NvEncoder/NvEncoderGL.h \
    Samples/NvCodec/NvEncoder/NvEncoder.h \
    %{buildroot}%{_includedir}/%{name}/

ln -sf %{_includedir}/%{name}/cuviddec.h Samples/NvCodec/NvDecoder/cuviddec.h
ln -sf %{_includedir}/%{name}/nvcuvid.h Samples/NvCodec/NvDecoder/nvcuvid.h
ln -sf %{_includedir}/%{name}/NvDecoder.h Samples/NvCodec/NvDecoder/NvDecoder.h
ln -sf %{_includedir}/%{name}/nvEncodeAPI.h Samples/NvCodec/NvEncoder/nvEncodeAPI.h
ln -sf %{_includedir}/%{name}/NvEncoderCuda.h Samples/NvCodec/NvEncoder/NvEncoderCuda.h
ln -sf %{_includedir}/%{name}/NvEncoderGL.h Samples/NvCodec/NvEncoder/NvEncoderGL.h
ln -sf %{_includedir}/%{name}/NvEncoder.h Samples/NvCodec/NvEncoder/NvEncoder.h

%files
%license LicenseAgreement.pdf
%doc doc/*.pdf *.txt
%{_includedir}/%{name}
 
%files samples
%doc Samples

%changelog
* Thu Jan 03 2019 Simone Caronni <negativo17@gmail.com> - 1:8.2.16-1
- Update to 8.2.16.

* Tue Apr 24 2018 Simone Caronni <negativo17@gmail.com> - 1:8.1.24-1
- Update to 8.1.24, do not add legacy samples.
- Update SPEC file.
- Require CUDA development package for 8.1.

* Thu Jun 22 2017 Simone Caronni <negativo17@gmail.com> - 1:8.0.14-1
- Update to 8.0.14.
- Do not add license also to samples, as it requires the base package.
- Requires driver 378.13+.
- Add NVDECODE headers and require nvidia-driver-devel for unversioned shared
  libraries.

* Sun Jan 08 2017 Simone Caronni <negativo17@gmail.com> - 1:7.1.9-1
- Update to 7.1.9.

* Fri Aug 19 2016 Simone Caronni <negativo17@gmail.com> - 7.0.1-1
- Update to 7.0.1.
- Runtime requires drivers 367.35+ and adds support for Pascal GPUs.

* Wed Jan 06 2016 Simone Caronni <negativo17@gmail.com> - 6.0.1-1
- Update to 6.0.1.

* Fri Apr 10 2015 Simone Caronni <negativo17@gmail.com> - 5.0.1-1
- First build.
