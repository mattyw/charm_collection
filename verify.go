package main

import (
	"fmt"
	"launchpad.net/juju-core/charm"
	"os"
	"path/filepath"
)

func main() {
	var charmDir string
	if len(os.Args) == 2 {
		charmDir = os.Args[1]

	}
	if charmDir == "" {
		fmt.Println("usage: %s charm_dir", filepath.Base(os.Args[0]))
		os.Exit(1)
	}

	ch, err := charm.ReadDir(charmDir)

	if err != nil {
		fmt.Println("Charm Error", err)
		os.Exit(1)
	} else {
		fmt.Println("Charm Success", ch)
	}

	meta := ch.Meta()

	for name, rel := range meta.Requires {
		fmt.Println("Required relation", name, rel.Interface, rel.Scope)
	}
}
