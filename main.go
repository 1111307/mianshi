package main

import (
	"context"
	"fmt"
	"net/http"
	"time"
)

func main() {
	var s string
	fmt.Scan(&s)
	fmt.Print(lengthOfLongestSubstring(s))

	var timeduration time.Duration
	timeduration = 10 * time.Second

	ctx, cancel := context.WithTimeout(context.Background(), timeduration)
	defer cancel()
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, "127.0.0.1:8081/new/get", nil)
	if err != nil {
		return
	}

	client := &http.Client{Timeout: 30 * time.Second}

	resp, err := client.Do(req)

	if resp.StatusCode != http.StatusOK {
		fmt.Print("request fail")
	}
}

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}

	Max := 0
	l, r := 0, 0
	m := make(map[byte]int, 0)

	for r < len(s) {
		if m[s[r]] == 0 {
			m[s[r]]++
			Max = max(Max, r-l+1)
			r++
			continue
		}

		for l < r {
			if s[l] == s[r] {
				m[s[l]]--
				l++
				break
			}
			m[s[l]]--
			l++
		}
		m[s[r]]++
		r++
	}

	return Max

}
