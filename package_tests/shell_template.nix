with import <nixpkgs> {};

let
  mach-nix = import (
    builtins.fetchGit {
      url = "https://github.com/DavHau/mach-nix/";
      ref = "2.2.0";
    }
  );

  customPython = mach-nix.mkPython {
    python = pkgs.python37;
    requirements = ''
      %s
    '';
  };
in

pkgs.mkShell {
  buildInputs = [
    customPython
  ];
}
