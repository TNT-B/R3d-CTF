from flask import Blueprint, render_template

from CTFd.utils import config
from CTFd.utils.config.visibility import scores_visible
from CTFd.utils.decorators.visibility import (
    check_account_visibility,
    check_score_visibility,
)
# from CTFd.utils.decorators import authed_only
# from CTFd.utils.helpers import get_infos
# from CTFd.utils.scores import get_standings
# from CTFd.utils.user import is_admin

testdocument = Blueprint("testdocument", __name__)


@testdocument.route("/testdocument")
def document_view():
    return render_template("document.html")
