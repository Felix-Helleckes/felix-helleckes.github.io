import { GoGitMerge, GoGitPullRequest } from 'react-icons/go';
import oss from '../../data/oss.json';

const formatDate = (iso: string) =>
  new Date(iso).toLocaleDateString('en-GB', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
  });

/**
 * Pull requests and issues in repositories Felix does not own. The numbers
 * come from src/data/oss.json, refreshed daily by the "Open-source stats"
 * workflow.
 */
const OpenSourceCard = () => {
  if (oss.merged + oss.open === 0) {
    return null;
  }

  return (
    <div className="col-span-1 lg:col-span-2">
      <div className="card bg-base-200 shadow-xl border border-base-300">
        <div className="card-body p-8">
          <div className="flex items-center space-x-3 mb-6">
            <div className="flex items-center justify-center w-12 h-12 bg-primary/10 rounded-xl">
              <GoGitPullRequest className="text-2xl" />
            </div>
            <div className="min-w-0 flex-1">
              <h3 className="text-base sm:text-lg font-bold text-base-content">
                Open-source contributions
              </h3>
              <div className="text-base-content/60 text-xs sm:text-sm mt-1">
                AI-assisted with Claude Code · in repositories I don't own
              </div>
            </div>
          </div>

          <div className="flex flex-wrap items-baseline gap-x-3 gap-y-1 mb-6">
            <span className="text-4xl font-bold text-base-content">
              {oss.merged}
            </span>
            <span className="text-base-content">merged pull requests</span>
            <span className="text-base-content/60 text-sm">
              · {oss.open} more in review · {oss.issues} issues reported
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="card shadow-md card-sm bg-base-100">
              <div className="p-6">
                <h4 className="font-medium opacity-60 mb-3">Repositories</h4>
                <ul className="space-y-3 text-sm">
                  {oss.repos.map((repo) => (
                    <li key={repo.name} className="text-base-content">
                      <a
                        href={repo.url}
                        target="_blank"
                        rel="noreferrer"
                        className="link link-hover break-all"
                      >
                        {repo.name}
                      </a>
                      <div className="text-xs text-base-content/60">
                        {[
                          repo.merged > 0 && `${repo.merged} merged`,
                          repo.open > 0 && `${repo.open} in review`,
                        ]
                          .filter(Boolean)
                          .join(' · ')}
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            <div className="card shadow-md card-sm bg-base-100">
              <div className="p-6">
                <h4 className="font-medium opacity-60 mb-3">Latest merged</h4>
                <ul className="space-y-3 text-sm">
                  {oss.latestMerged.map((pr) => (
                    <li key={pr.url} className="flex gap-2 text-base-content">
                      <GoGitMerge className="shrink-0 mt-0.5 opacity-60" />
                      <div className="min-w-0">
                        <a
                          href={pr.url}
                          target="_blank"
                          rel="noreferrer"
                          className="link link-hover"
                        >
                          {pr.title}
                        </a>
                        <div className="text-xs text-base-content/60">
                          {pr.repo} · {formatDate(pr.mergedAt)}
                        </div>
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          <p className="text-xs text-base-content/60 mt-6">
            Counted daily from the GitHub search API · last change{' '}
            {formatDate(oss.updatedAt)}
          </p>
        </div>
      </div>
    </div>
  );
};

export default OpenSourceCard;
