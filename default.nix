with import <nixpkgs> {};
pkgs.mkShell {
  buildInputs = [
    bashInteractive
    python2
    python2Packages.pystache
    python2Packages.simplejson
    # shinyedit
    python2Packages.tkinter
  ];
}
