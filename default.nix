with import <nixpkgs> {};
pkgs.mkShell {
  buildInputs = [
    bashInteractive
    imagemagick
    python2
    python2Packages.pystache
    python2Packages.simplejson
    # shinyedit
    python2Packages.tkinter
  ];
}
