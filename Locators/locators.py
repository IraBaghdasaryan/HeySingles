from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class WelcomePageLocators:
    _joinus_button = {"by": By.ACCESSIBILITY_ID, "value": "welcomeLoginButton"}
    _login_button = {"by": By.ACCESSIBILITY_ID, "value": "welcomeRegistrationButton"}


class LoginPageLocators:
    _username_input = {"by": By.ACCESSIBILITY_ID, "value": "signInUsernameInput"}
    _password_input = {"by": By.ACCESSIBILITY_ID, "value": "signInPasswordInput"}
    _seepassword_button = {"by": By.ACCESSIBILITY_ID, "value": "signInPasswordInputEye"}
    _signin_button = {"by": By.ACCESSIBILITY_ID, "value": "signInLoginButton"}
    _back_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _facebook_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _vk_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _forgot_password_button = {"by": By.ACCESSIBILITY_ID, "value": "signInForgetPassword"}
    _signup_button = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _hs_logo = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _wrong_username = {"by": By.ACCESSIBILITY_ID, "value": ""}
    _wrong_pass = {"by": By.ACCESSIBILITY_ID, "value": ""}


class SwipePageLocators:
    _photo_ = {"by": By.ACCESSIBILITY_ID, "value": "cardUserImage"}
    _dislike_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeDislikeIcon"}
    _gift_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeGiftIcon"}
    _like_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeLikeIcon"}
    _filter_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeFilterIcon"}
    _undo_button = {"by": By.ACCESSIBILITY_ID, "value": "swipeUndoIcon"}
    _location_value = {"by": By.ACCESSIBILITY_ID, "value": "userCardLocationValue"}
    _block_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardBlockOrReport"}
    _gift_card_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardSendGiftCardButtonText"}
    _user_name = {"by": By.ACCESSIBILITY_ID, "value": "cardUserFirstName"}
    _user_age = {"by": By.ACCESSIBILITY_ID, "value": "cardUserAge"}
    _report_abuse_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardReportAbuseButton"}
    _report_block_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardReportAbuseButton"}
    _cancel_button = {"by": By.ACCESSIBILITY_ID, "value": "userCardBlockOrReportCancelButton"}


class MenuLocators:
    _search_button = {"by": By.ACCESSIBILITY_ID,  "value": "//android.widget.FrameLayout[@content-desc=\"Search, tab, 1 out of 4\"]/android.widget.TextView"}
    _swipe_button = {"by": By.ACCESSIBILITY_ID, "value": "//android.widget.FrameLayout[@content-desc=\"Search, tab, 1 out of 4\"]/android.widget.TextView"}
    _chat_button = {"by": By.ACCESSIBILITY_ID, "value": "//android.widget.FrameLayout[@content-desc=\"Chat, tab, 3 out of 4\"]/android.widget.ImageView"}
    _me_button = {"by": By.ACCESSIBILITY_ID, "value": "//android.widget.FrameLayout[@content-desc=\"Me, tab, 4 out of 4\"]/android.widget.ImageView"}


class SwipeFilterLocator:
    _save_button = {"by": By.ACCESSIBILITY_ID, "value": "filterHeaderCheckIcon"}
    _show_men_button = {"by": By.ACCESSIBILITY_ID, "value": "filterGenderButtonMen"}
    _show_women_button = {"by": By.ACCESSIBILITY_ID, "value": "filterGenderButtonWomen"}
    _show_both_button = {"by": By.ACCESSIBILITY_ID, "value": "filterGenderButtonBoth"}
    _location_button = {"by": By.ACCESSIBILITY_ID, "value": "filterLocationInputField"}



class SwipeLocationLocators:
    _search_box = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteSearchInput"}
    _cancel_button = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteCancel"}
    _current_location = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteCurrentLocationRow"}
    _line_results = {"by": By.ACCESSIBILITY_ID, "value": "cityAutocompleteCurrentLocationRow"}




class MyProfile:
    _settings_button = {"by": By.ACCESSIBILITY_ID, "value": "mainProfileSettingsIcon"}
    _need_help_button = {"by": By.ACCESSIBILITY_ID, "value": "//android.view.View[@content-desc=\"%3Fgclid%3DEAIaIQobChMIm8_bjYPY7wIVCca7CB1OOAP5EAEYASAAEgKyzPD_BwE\"]/android.view.View"}


class Settings:
    _basic_info_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemBasic Info"}
    _fb_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemJoin HeySingles on Facebook"}
    _help_centre_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemHelp center"}
    _report_problem_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemReport a problem"}
    _account_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemAccount"}
    _linked_account_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemLinked Accounts"}
    _notifications_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemNotifications"}
    _privacy_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemPrivacy"}
    _invisible_mode_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemInvisible mode"}
    _verification_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemVerifications"}
    _payment_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemPayment Settings"}
    _language_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemApp Language"}
    _blocked_users_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemBlocked users"}
    _terms_of_use_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemTerms of Use"}
    _about_button = {"by": By.ACCESSIBILITY_ID, "value": "allMainSettingsItemAbout"}


class Account:
    _sign_out_button = {"by":By.ACCESSIBILITY_ID, "value": "signOutButton"}
    _hide_account_button = {"by":By.ACCESSIBILITY_ID, "value": "accountSettingsHideAccountSwitch"}
    _back_button = {"by": By.ACCESSIBILITY_ID, "value": "accountSettingsHideAccountSwitch"}

class BlockedUsers:
    _edit_button = {"by": By.ACCESSIBILITY_ID, "value": "Edit"}
    _cancel_button = {"by": By.ACCESSIBILITY_ID, "value": "Cancel"}
    _unblock_selected_button = {"by": By.ACCESSIBILITY_ID, "value": "blockedUsersUnblockSelectedButton"}
    _back_button = {"by": By.ACCESSIBILITY_ID, "value": "backButton"}

