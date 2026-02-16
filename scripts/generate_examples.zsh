#! /usr/bin/env zsh
# vim: filetype=zsh: tabstop=3: shiftwidth=3: noexpandtab:

emulate zsh \
	-o no__bare_glob_qual   +o no__glob             +o ____glob_subst \
	-o no__case_glob        +o ____glob_assign      -o ____null_glob \
	-o ____err_exit         +o ____globdots         -o ____numeric_glob_sort \
	-o ____extendedglob     -o ____glob_star_short  -o no__unset

# Run all example scripts and generate SVG outputs.
# Run from the project root:
#   ./scripts/generate_examples.zsh

typeset ROOT_DIR EXAMPLES_DIR OUT_DIR

typeset -gx PYTHONPATH

ROOT_DIR=${(%):-'%x'}
ROOT_DIR=${ROOT_DIR:a}
ROOT_DIR=${ROOT_DIR:h:h}

EXAMPLES_DIR=${ROOT_DIR}/examples

OUT_DIR=${EXAMPLES_DIR}/generated_svgs

PYTHONPATH=${ROOT_DIR}${PYTHONPATH:+:${PYTHONPATH}}

# print - "\n======> PYTHONPATH"
# print -l - "${(@As.:.)PYTHONPATH}"


##
mkdir -p "$OUT_DIR"

print -r -- "==> Generating SVGs into: $OUT_DIR"
print -r -- "==> Using python: ${(q)${PYTHON:-python}}"
print -r -- ""

# Find all example .py files under the three level folders (ignore _shared).
typeset -a files

files=( ${EXAMPLES_DIR}/level-*/*.py(#q-.:a) )

if (( ${#files} == 0 )); then
	print -r -- "No example scripts found under:"
	print -r -- "  $EXAMPLES_DIR/level-1-basic"
	print -r -- "  $EXAMPLES_DIR/level-2-intermediate"
	print -r -- "  $EXAMPLES_DIR/level-3-advanced"
	exit 1
fi

typeset -i ok=0
typeset -i fail=0

cd "${EXAMPLES_DIR}"

for f in "${(@)files}"; do
	print -r -- "----"
	print -r -- "Running: ${f#$ROOT_DIR/}"

	# Use system python by default; allow override via $PYTHON.
	"${PYTHON:-python}" "$f" || true
done

print -r -- "----"
print -r -- "Done. OK=$ok FAIL=$fail"
(( fail == 0 ))

