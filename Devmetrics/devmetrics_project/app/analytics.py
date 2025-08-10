def compute_metrics(repos):
    total_repos = len(repos)
    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
    total_forks = sum(repo.get("forks_count", 0) for repo in repos)
    total_open_issues = sum(repo.get("open_issues_count", 0) for repo in repos)
    avg_stars = total_stars / total_repos if total_repos else 0

    score = (
        total_repos * 2 +
        total_stars * 3 +
        total_forks * 1.5 -
        total_open_issues * 0.5
    )
    score = max(0, round(score, 2))

    return {
        "total_repos": total_repos,
        "total_stars": total_stars,
        "total_forks": total_forks,
        "total_open_issues": total_open_issues,
        "avg_stars": round(avg_stars, 2),
        "score": score
    }
