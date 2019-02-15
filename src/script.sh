#!/bin/bash
../Stockfish/src/stockfish << EOF
uci
ucinewgame
position startpos moves $1
go depth 7
go nodes 1
quit
EOF