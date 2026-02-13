{
  description = "mini-svg — Mini librería educativa SVG";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
    systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
    forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f system);
  in
  {
    devShells = forAllSystems (system:
      let
        pkgs = import nixpkgs { inherit system; };

        python = pkgs.python313;
      in
      {
        default = pkgs.mkShell {
          name = "mini-svg-devshell";

          packages = [
            python
            python.pkgs.pip
            python.pkgs.setuptools
            python.pkgs.wheel

            # Dev tools
            python.pkgs.pytest
            python.pkgs.ruff
            python.pkgs.black
            python.pkgs.mypy
          ];

          # Aquí está la clave
          shellHook = ''
            export PYTHONPATH="$PWD/src''${PYTHONPATH:+:}$PYTHONPATH"

            echo "mini-svg devShell listo"
            echo "Python: $(python --version)"
            echo "Import test:"
            python - <<EOF
from mini_svg import v1
print("mini_svg import OK")
EOF
          '';
        };
      }
    );
  };
}

