{ pkgs ? (import <nixpkgs> {}).pkgs }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python27Packages.scapy
  ];
}
