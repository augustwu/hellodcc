#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A hellodcc.taskapp beat -l INFO
